from Generate_Shape import Genertor_Shape as gs
def run():
    runner = True
    while (runner):
        shape = input("Enter your's Shape Name: ")
        match shape:
            case "exit":
                runner = False
            case "Triangle":
                return gs.Generate_Triangle()
            case "Circle":
                return gs.Generate_Circle()
            case "Square":
                return gs.Generate_Square()
            case "Hexagon":
                return gs.Generate_Hexagon()
            case "Rectangle":
                return gs.Generate_Rectangle()
shape = run()
print(shape)