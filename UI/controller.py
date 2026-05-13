import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._stato = None

    def handleCalcola(self, e):

        self._view._txt_result.controls.clear()
        anno = int(self._view._txtAnno.value)
        self._model.buildGraph(anno)
        self._view._txt_result.controls.append(ft.Text("Grafo creato"))
        self._view._txt_result.controls.append(
            ft.Text(f"Il grafo contiene {self._model.getNumNodes()} nodi e {self._model.getNumEdges()} archi e Connessioni {self._model.getConnesso()}."))

        gradi = self._model.getGrado()

        for n in gradi:
            self._view._txt_result.controls.append(
                ft.Text(f"{n[0]} : {n[1]} vicini")
            )

        self._view.update_page()

    def fillStato(self):
        nodi = self._model._nodes
        for n in nodi:
            self._view._ddStato.options.append(ft.dropdown.Option(
                key = n.CCode,
                text = n.StateNme,
                data = n,
                on_click=self.read_stato
            ))
        self._view.update_page()

    def read_stato(self,e):
        self._stato = e.control.data

    def handleStatiRaggiungibili(self,e):

        self._view._txt_result.controls.clear()
        lista = self._model.getTree(self._stato)
        for l in lista:
            self._view._txt_result.controls.append(
                ft.Text(l)
            )
        self._view._txt_result.controls.append(
            ft.Text(len(lista))
        )
        self._view.update_page()

        visited = set()
        component = self._model.dfs_recursive(self._stato, visited)
        self._view._txt_result.controls.append(
            ft.Text("----------------------------")
        )
        for c in component:
            self._view._txt_result.controls.append(
                ft.Text(c)
            )
        self._view._txt_result.controls.append(
            ft.Text(len(component))
        )
        self._view.update_page()

