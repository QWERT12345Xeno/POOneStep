from datetime import datetime, timedelta


class Playlist:
    def __init__(self, i, n, d):
        self.set_id(i)
        self.set_nome(n)
        self.set_data(d)

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_data(self):
        return self.__data

    def set_id(self, i):
        if type(i) != int or i <= 0:
            raise ValueError("Id da playlist invalido")
        self.__id = i

    def set_nome(self, n):
        if type(n) != str or n.strip() == "":
            raise ValueError("Nome da playlist invalido")
        self.__nome = n.strip()

    def set_data(self, d):
        if type(d) != datetime:
            raise ValueError("Data invalida")
        self.__data = d

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__data.strftime('%d/%m/%Y')}"


class Video:
    def __init__(self, i, i_p, t, d):
        self.set_id(i)
        self.set_id_playlist(i_p)
        self.set_titulo(t)
        self.set_duracao(d)
        self.__num_visualizacoes = 0

    def get_id(self):
        return self.__id

    def get_id_playlist(self):
        return self.__id_playlist

    def get_titulo(self):
        return self.__titulo

    def get_duracao(self):
        return self.__duracao

    def get_num_visualizacoes(self):
        return self.__num_visualizacoes

    def set_id(self, i):
        if type(i) != int or i <= 0:
            raise ValueError("Id do video invalido")
        self.__id = i

    def set_id_playlist(self, i_p):
        if type(i_p) != int or i_p <= 0:
            raise ValueError("Id da playlist invalido")
        self.__id_playlist = i_p

    def set_titulo(self, t):
        if type(t) != str or t.strip() == "":
            raise ValueError("Titulo invalido")
        self.__titulo = t.strip()

    def set_duracao(self, d):
        if type(d) != timedelta or d.total_seconds() <= 0:
            raise ValueError("Duracao invalida")
        self.__duracao = d

    def set_num_visualizacoes(self, n):
        if type(n) != int or n < 0:
            raise ValueError("Numero de visualizacoes invalido")
        self.__num_visualizacoes = n

    def Visualizar(self):
        self.__num_visualizacoes += 1

    def NumVisualizacoes(self):
        return self.__num_visualizacoes

    def __str__(self):
        return (f"{self.__id} - {self.__titulo} - Playlist {self.__id_playlist} - "
                f"{self.__duracao} - {self.__num_visualizacoes} visualizacoes")


class UI:
    __playlists = []
    __videos = []

    @classmethod
    def main(cls):
        op = 0
        while op != 7:
            op = cls.menu()
            if op == 1:
                cls.inserir_playlist()
            elif op == 2:
                cls.listar_playlists()
            elif op == 3:
                cls.inserir_video()
            elif op == 4:
                cls.listar_videos()
            elif op == 5:
                cls.visualizar_video()
            elif op == 6:
                cls.video_mais_visto()
            elif op == 7:
                print("Fim")
            else:
                print("Opcao invalida")

    @classmethod
    def menu(cls):
        print()
        print("1 - Inserir playlist")
        print("2 - Listar playlists")
        print("3 - Inserir video")
        print("4 - Listar videos")
        print("5 - Visualizar video")
        print("6 - Video mais visto")
        print("7 - Fim")
        try:
            return int(input("Opcao: "))
        except ValueError:
            return 0

    @classmethod
    def buscar_playlist(cls, id):
        for p in cls.__playlists:
            if p.get_id() == id:
                return p
        return None

    @classmethod
    def buscar_video(cls, id):
        for v in cls.__videos:
            if v.get_id() == id:
                return v
        return None

    @classmethod
    def inserir_playlist(cls):
        try:
            i = int(input("Id: "))
            if cls.buscar_playlist(i) is not None:
                print("Ja existe uma playlist com esse id")
                return
            n = input("Nome: ")
            d = datetime.strptime(input("Data de criacao (dd/mm/aaaa): "), "%d/%m/%Y")
            cls.__playlists.append(Playlist(i, n, d))
            print("Playlist inserida")
        except ValueError as e:
            print("Erro:", e)

    @classmethod
    def listar_playlists(cls):
        if len(cls.__playlists) == 0:
            print("Nenhuma playlist cadastrada")
            return
        for p in sorted(cls.__playlists, key=lambda p: p.get_data()):
            print(p)

    @classmethod
    def inserir_video(cls):
        try:
            i = int(input("Id do video: "))
            if cls.buscar_video(i) is not None:
                print("Ja existe um video com esse id")
                return
            i_p = int(input("Id da playlist: "))
            if cls.buscar_playlist(i_p) is None:
                print("Playlist nao encontrada")
                return
            t = input("Titulo: ")
            s = int(input("Duracao em segundos: "))
            cls.__videos.append(Video(i, i_p, t, timedelta(seconds=s)))
            print("Video inserido")
        except ValueError as e:
            print("Erro:", e)

    @classmethod
    def listar_videos(cls):
        if len(cls.__videos) == 0:
            print("Nenhum video cadastrado")
            return
        for v in sorted(cls.__videos, key=lambda v: v.get_duracao()):
            print(v)

    @classmethod
    def visualizar_video(cls):
        try:
            i = int(input("Id do video: "))
        except ValueError:
            print("Id invalido")
            return
        v = cls.buscar_video(i)
        if v is None:
            print("Video nao encontrado")
        else:
            v.Visualizar()
            print("Visualizacao registrada")

    @classmethod
    def video_mais_visto(cls):
        if len(cls.__videos) == 0:
            print("Nenhum video cadastrado")
            return
        mais = cls.__videos[0]
        for v in cls.__videos:
            if v.NumVisualizacoes() > mais.NumVisualizacoes():
                mais = v
        print(mais)


UI.main()
