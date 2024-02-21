from jsonschema import validate
from jsonschema.exceptions import ValidationError


users = {1:{"birthYear":1968,"firstName":"Brian","lastName":"Bright","group":"user"},2:{"birthYear":1998,"firstName":"Casey","lastName":"Stein","group":"premium"},3:{"birthYear":1995,"firstName":"Anne","lastName":"Burch","group":"user"},4:{"birthYear":1995,"firstName":"Terry","lastName":"Hodges","group":"user"},5:{"birthYear":1967,"firstName":"Candice","lastName":"Woods","group":"user"},6:{"birthYear":2009,"firstName":"Michelle","lastName":"Castaneda","group":"user"},7:{"birthYear":1990,"firstName":"Jacqueline","lastName":"Branch","group":"user"},8:{"birthYear":1994,"firstName":"Henry","lastName":"Mullins","group":"user"},9:{"birthYear":1960,"firstName":"Michelle","lastName":"Montgomery","group":"user"},10:{"birthYear":1996,"firstName":"Melissa","lastName":"Baker","group":"user"},11:{"birthYear":1992,"firstName":"Bradley","lastName":"Reeves","group":"user"},12:{"birthYear":1966,"firstName":"Jason","lastName":"Carrillo","group":"user"},13:{"birthYear":2005,"firstName":"Eileen","lastName":"Schmidt","group":"user"},14:{"birthYear":1965,"firstName":"Mario","lastName":"Harrell","group":"user"},15:{"birthYear":1999,"firstName":"Steven","lastName":"Douglas","group":"user"},16:{"birthYear":1960,"firstName":"Andrew","lastName":"Wilson","group":"user"},19:{"birthYear":1965,"firstName":"Jason","lastName":"Green","group":"user"},19:{"birthYear":1965,"firstName":"Tanya","lastName":"Davis","group":"user"},19:{"birthYear":1998,"firstName":"Lance","lastName":"Wood","group":"user"},20:{"birthYear":1960,"firstName":"John","lastName":"Wong","group":"user"},21:{"birthYear":2007,"firstName":"Lisa","lastName":"Novak","group":"user"},22:{"birthYear":1995,"firstName":"Barbara","lastName":"Knight","group":"user"},23:{"birthYear":1991,"firstName":"Candace","lastName":"Valencia","group":"user"},24:{"birthYear":1968,"firstName":"Cynthia","lastName":"Lang","group":"user"},25:{"birthYear":2009,"firstName":"Natalie","lastName":"Dyer","group":"user"},26:{"birthYear":1999,"firstName":"Tiffany","lastName":"Green","group":"user"},27:{"birthYear":1963,"firstName":"Daniel","lastName":"Bell","group":"user"},28:{"birthYear":1999,"firstName":"John","lastName":"Murray","group":"premium"},29:{"birthYear":1996,"firstName":"Leslie","lastName":"Nelson","group":"user"},30:{"birthYear":1996,"firstName":"Shelia","lastName":"Fisher","group":"user"},31:{"birthYear":2002,"firstName":"Jonathan","lastName":"Payne","group":"user"},32:{"birthYear":1962,"firstName":"Stacy","lastName":"Simmons","group":"user"},33:{"birthYear":1962,"firstName":"Mark","lastName":"Adams","group":"user"},34:{"birthYear":2005,"firstName":"Michael","lastName":"Tate","group":"user"},35:{"birthYear":1999,"firstName":"Brett","lastName":"Miller","group":"user"},36:{"birthYear":2002,"firstName":"Dennis","lastName":"Roberts","group":"user"},37:{"birthYear":2003,"firstName":"Lori","lastName":"Long","group":"user"},38:{"birthYear":1996,"firstName":"Peter","lastName":"Barker","group":"user"},39:{"birthYear":1969,"firstName":"Scott","lastName":"Sawyer","group":"user"},40:{"birthYear":1990,"firstName":"Emily","lastName":"Wyatt","group":"user"},41:{"birthYear":1991,"firstName":"Brandon","lastName":"Calderon","group":"user"},42:{"birthYear":1999,"firstName":"Jerry","lastName":"Baldwin","group":"user"},43:{"birthYear":1966,"firstName":"Scott","lastName":"Robertson","group":"premium"},44:{"birthYear":1998,"firstName":"Brian","lastName":"Thompson","group":"user"},45:{"birthYear":1960,"firstName":"Juan","lastName":"Smith","group":"user"},46:{"birthYear":1965,"firstName":"Richard","lastName":"Mckenzie","group":"user"},47:{"birthYear":1962,"firstName":"Donald","lastName":"Watson","group":"user"},48:{"birthYear":1968,"firstName":"John","lastName":"Alexander","group":"user"},49:{"birthYear":1960,"firstName":"Bryan","lastName":"Williams","group":"user"},50:{"birthYear":2001,"firstName":"Wesley","lastName":"Lee","group":"user"},51:{"birthYear":1991,"firstName":"Matthew","lastName":"Miller","group":"user"},52:{"birthYear":1967,"firstName":"Drew","lastName":"Brown","group":"user"},53:{"birthYear":1997,"firstName":"Kyle","lastName":"Adams","group":"user"},54:{"birthYear":2002,"firstName":"Carolyn","lastName":"Holder","group":"user"},55:{"birthYear":1997,"firstName":"Kaitlyn","lastName":"Allen","group":"user"},56:{"birthYear":1992,"firstName":"Robert","lastName":"Navarro","group":"user"},57:{"birthYear":1995,"firstName":"Emily","lastName":"Wade","group":"user"},58:{"birthYear":1995,"firstName":"Tiffany","lastName":"Black","group":"user"},59:{"birthYear":1993,"firstName":"John","lastName":"Keller","group":"premium"},60:{"birthYear":1965,"firstName":"Wayne","lastName":"Diaz","group":"user"},61:{"birthYear":1996,"firstName":"Michael","lastName":"Stanton","group":"user"},62:{"birthYear":1965,"firstName":"Ashlee","lastName":"Henry","group":"user"},63:{"birthYear":1963,"firstName":"William","lastName":"Fischer","group":"user"},64:{"birthYear":1999,"firstName":"Christine","lastName":"Anderson","group":"user"},65:{"birthYear":1961,"firstName":"James","lastName":"Frederick","group":"user"},66:{"birthYear":1992,"firstName":"Dr.","lastName":"John","group":"user"},67:{"birthYear":2001,"firstName":"Kevin","lastName":"Wagner","group":"user"},68:{"birthYear":1967,"firstName":"Natalie","lastName":"Kelley","group":"user"},69:{"birthYear":2009,"firstName":"Rebekah","lastName":"Owens","group":"user"},70:{"birthYear":1998,"firstName":"Steven","lastName":"Young","group":"user"},71:{"birthYear":1970,"firstName":"Tiffany","lastName":"Alexander","group":"premium"},72:{"birthYear":1969,"firstName":"Ryan","lastName":"Turner","group":"user"},73:{"birthYear":1999,"firstName":"Elizabeth","lastName":"Manning","group":"user"},74:{"birthYear":2001,"firstName":"Timothy","lastName":"Johnson","group":"user"},75:{"birthYear":1968,"firstName":"Ashley","lastName":"Baker","group":"user"},76:{"birthYear":1964,"firstName":"Christopher","lastName":"Garcia","group":"user"},77:{"birthYear":1999,"firstName":"Cassandra","lastName":"Miller","group":"user"},78:{"birthYear":1998,"firstName":"Rose","lastName":"Walker","group":"user"},79:{"birthYear":1998,"firstName":"Willie","lastName":"Cross","group":"user"},80:{"birthYear":2001,"firstName":"Joseph","lastName":"Combs","group":"premium"},81:{"birthYear":1999,"firstName":"Natasha","lastName":"Simmons","group":"user"},82:{"birthYear":1963,"firstName":"Natalie","lastName":"Cooper","group":"user"},83:{"birthYear":2002,"firstName":"Amber","lastName":"Rodriguez","group":"user"},84:{"birthYear":1997,"firstName":"Stanley","lastName":"Smith","group":"user"},85:{"birthYear":2007,"firstName":"Jacob","lastName":"Garcia","group":"user"},86:{"birthYear":1963,"firstName":"Joseph","lastName":"Willis","group":"user"},87:{"birthYear":1961,"firstName":"Gary","lastName":"Macdonald","group":"user"},88:{"birthYear":1990,"firstName":"Lisa","lastName":"Williams","group":"user"},89:{"birthYear":1967,"firstName":"Chad","lastName":"Williams","group":"user"},90:{"birthYear":2003,"firstName":"Patricia","lastName":"Bailey","group":"user"},91:{"birthYear":1967,"firstName":"Heather","lastName":"Garner","group":"user"},92:{"birthYear":2003,"firstName":"Heather","lastName":"Mcintyre","group":"premium"},93:{"birthYear":2007,"firstName":"Emily","lastName":"Frazier","group":"user"},94:{"birthYear":1960,"firstName":"Debra","lastName":"Stewart","group":"user"},95:{"birthYear":1992,"firstName":"Carl","lastName":"Williams","group":"user"},96:{"birthYear":1997,"firstName":"Desiree","lastName":"Wright","group":"user"},97:{"birthYear":2005,"firstName":"Charlene","lastName":"Chavez","group":"user"},98:{"birthYear":1996,"firstName":"Daniel","lastName":"Sanchez","group":"user"},99:{"birthYear":1969,"firstName":"Andrea","lastName":"Wilson","group":"user"},100:{"birthYear":2000,"firstName":"Robert","lastName":"Bishop","group":"user"}}

class _User:
    def __init__(self):
        pass

    schema_patch = {
        "type": "object",
        "properties": {
            "firstName": {"type": "string"},
            "lastName": {"type": "string"},
            "birthYear": {"type": "number"},
            "group": {"enum": ["user", "premium", "admin"]},
        },
        "minProperties": 1,
        "additionalProperties": False
    }
    schema_post = {
        "type": "object",
        "properties": {
            "firstName": {"type": "string"},
            "lastName": {"type": "string"},
            "birthYear": {"type": "number"},
            "group": {"enum": ["user", "premium", "admin"]},
        },
        "required": ["firstName", "lastName", "birthYear", "group"],
        "additionalProperties": False
    }

    def validate_patch(self, data: dict) -> bool:
        try:
            validate(instance=data, schema=self.schema_patch)
            return True
        except ValidationError as e:
            return False

    def validate_post(self, data: dict) -> bool:
        try:
            validate(instance=data, schema=self.schema_post)
            return True
        except ValidationError as e:
            return False


User = _User()
