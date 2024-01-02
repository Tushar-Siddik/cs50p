file_name = (input("File name: ")).lower().strip()

extension = file_name.split(".")

match extension[-1]:
    case "gif" | "jpeg" | "png":
        print("image/"+ extension[-1])
    case "jpg":
        print("image/jpeg")
    case "pdf" | "zip":
        print("application/"+ extension[-1])
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")
