import asyncio
import re
import aiohttp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.progressbar import ProgressBar

from config import HEADERS, PLATAFORMAS, FIRMAS_ERROR_GLOBAL

class OSINTApp(App):
    def build(self):
        self.title = "OSINT Profile Checker"
        self.resultados = []
        
        # Layout principal
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Encabezado
        root.add_widget(Label(text="[b]OSINT PROFILE CHECKER[/b]", markup=True, size_hint_y=None, height=40))

        # Campo de entrada
        self.input_query = TextInput(
            hint_text="Ingrese usuario, nick o correo...",
            multiline=False,
            size_hint_y=None,
            height=45
        )
        root.add_widget(self.input_query)

        # Botón de búsqueda
        self.btn_buscar = Button(
            text="Iniciar Búsqueda",
            size_hint_y=None,
            height=50,
            background_color=(0.2, 0.6, 1, 1)
        )
        self.btn_buscar.bind(on_press=self.iniciar_busqueda)
        root.add_widget(self.btn_buscar)

        # Barra de progreso
        self.progress_bar = ProgressBar(max=len(PLATAFORMAS), value=0, size_hint_y=None, height=20)
        root.add_widget(self.progress_bar)

        # Label de Estado
        self.lbl_estado = Label(text="Estado: Listo", size_hint_y=None, height=30)
        root.add_widget(self.lbl_estado)

        # Área de resultados con scroll
        self.scroll = ScrollView()
        self.lbl_resultados = Label(
            text="Los resultados aparecerán aquí...",
            markup=True,
            size_hint_y=None,
            alignment=('left', 'top')
        )
        self.lbl_resultados.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.scroll.add_widget(self.lbl_resultados)
        root.add_widget(self.scroll)

        return root

    def iniciar_busqueda(self, instance):
        valor = self.input_query.text.strip()
        if not valor:
            self.lbl_estado.text = "Error: Ingrese un término válido"
            return

        if "@" in valor:
            valor = valor.split("@")[0]

        self.btn_buscar.disabled = True
        self.progress_bar.max = len(PLATAFORMAS)
        self.progress_bar.value = 0
        self.lbl_resultados.text = "Iniciando consultas en paralelo...\n"
        self.lbl_estado.text = f"Buscando '{valor}'..."

        asyncio.ensure_future(self._ejecutar_busqueda(valor))

    async def _verificar_plataforma(self, session, semaphore, nombre, config_plat, valor):
        valor_limpio = valor.replace(" ", "").lower()
        url = config_plat["url"].format(valor_limpio)
        firmas_especificas = config_plat.get("firmas_error", [])

        async with semaphore:
            try:
                async with session.get(url, headers=HEADERS, timeout=6, allow_redirects=True) as resp:
                    if resp.status == 200:
                        html = (await resp.text(errors="ignore")).lower()

                        if any(f in html for f in firmas_especificas) or any(f in html for f in FIRMAS_ERROR_GLOBAL):
                            return None

                        plataforma_slug = re.sub(r"[^\w]", "", nombre.lower())
                        avatar_url = f"https://unavatar.io/{plataforma_slug}/{valor_limpio}"
                        return {"plataforma": nombre, "url": url, "avatar": avatar_url}
            except Exception:
                pass
            return None

    async def _ejecutar_busqueda(self, valor):
        connector = aiohttp.TCPConnector(ssl=False)
        semaphore = asyncio.Semaphore(12)  # Máximo 12 peticiones simultáneas
        encontrados = []

        async with aiohttp.ClientSession(connector=connector) as session:
            tareas = [
                self._verificar_plataforma(session, semaphore, nombre, config_plat, valor)
                for nombre, config_plat in PLATAFORMAS.items()
            ]

            for corrutina in asyncio.as_completed(tareas):
                res = await corrutina
                self.progress_bar.value += 1

                if res:
                    encontrados.append(res)
                    self.lbl_resultados.text += f"• [color=00ff00]{res['plataforma']}[/color]: {res['url']}\n"

        self.lbl_estado.text = f"Finalizado. {len(encontrados)} perfiles encontrados."
        self.btn_buscar.disabled = False

if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(OSINTApp().async_run())
