from database.DB_connect import DBConnect
from model.arco import Arco
from model.country import Country


class DAO():

    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []
        query = """select c.StateAbb , c.CCode , c.StateNme 
                    from country c, contiguity cy
                    where (c.CCode = cy.state1no 
                    or c.CCode = cy.state2no)
                    group by c.StateAbb , c.CCode , c.StateNme """

        cursor.execute(query,)

        for row in cursor:
            res.append(Country(**row))
            # res.append(ArtObject(object_id=row["object_id"], ...))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getAllNodesAnno(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []
        query = """select c.StateAbb , c.CCode , c.StateNme 
                        from country c, contiguity cy
                        where (c.CCode = cy.state1no 
                        or c.CCode = cy.state2no)
                        and cy.year <= %s
                        group by c.StateAbb , c.CCode , c.StateNme """

        cursor.execute(query, (anno,))

        for row in cursor:
            res.append(Country(**row))
            # res.append(ArtObject(object_id=row["object_id"], ...))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getAllEdges(anno, idMap):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []
        query = """select cy.state1no as c1, cy.state2no as c2
                    from contiguity cy
                    where cy.year <= %s
                    and cy.conttype = 1
                    and cy.state1no < cy.state2no 
                    group by cy.state1ab , cy.state2ab  """

        cursor.execute(query , (anno,))

        for row in cursor:
            # res.append((o1, o2, peso))
            res.append(Arco(idMap[row["c1"]], idMap[row["c2"]]))

        cursor.close()
        conn.close()
        return res