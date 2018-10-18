from practico08.data import DatosSingleton
from practico08.data import Sala


class DatosSala(DatosSingleton):
    def alta(self, sala):

        """
        Da de alta a una sala y la devuelve
        :type sala: Sala
        :rtype: Sala
        """
        self.session.add(sala)
        self.session.commit()
        return sala

    def buscar_por_link(self, link_invitacion):
        """
        Busca una sala por link_invitacion y la devuelve. Si no la encuentra devuelve None
        :type codigo: string
        :rtype:Sala
        """
        s = self.session.query(Sala).filter(Sala.link_invitacion == link_invitacion).first()
        return s

    def buscar_por_id(self, id_sala):
        """
        Busca un usuario por id y lo devuelve
        :type id_sala:int
        :rtype: Sala
        """
        s = self.session.query(Sala).filter(Sala.id == id_sala).first()
        return s

    def modificar(self, sala):
        s = self.buscar_por_id(sala.id)
        s.votacion_vigente = sala.votacion_vigente
        s.link_invitacion = sala.link_invitacion
        self.session.commit()
        return s

    def todos(self):
        """
        Devuelve
        :return:
        """
        s = self.session.query(Sala).all()
        return s

    def borrar_todos(self):
        """
        Borra todos los socios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            salas = self.todos()
            for sala in salas:
                self.session.delete(sala)
            self.session.commit()
        except Exception:
            return False
        return True

    def buscar_por_id_admin(self, id_admin):
        sala = self.session.query(Sala).filter(Sala.id_admin == id_admin).first()
        return sala