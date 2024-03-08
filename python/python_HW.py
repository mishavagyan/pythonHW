while(True):
    fileName = input("Enter numeric name of file you want to open: ")
    try:
        if not fileName.isnumeric():
            raise ValueError('Represents a hidden bug, do not catch this')
        f = open(f"{fileName}.txt", "r")
        print(f.read())
        f.close()
        break
    except ValueError:
        print("Please enter valid file name")
    except FileNotFoundError:
        print(f"File named '{fileName}' doesn't exist")

while(True):
    answer = input("\nIf you want to write to this file enter '1'\nIf you want to write to a new file enter '2'\n")
    if answer == '1' or answer == '2':
        break
if answer == '1':
    f = open(f"{fileName}.txt", "a")
    content = input("New info: ")
    f.write(f"\n{content}")
    f.close()
else:
    b = True
    while(b):
        fileName = input("Enter numeric name of file you want to open: ")
        try:
            if not fileName.isnumeric():
                raise ValueError('Represents a hidden bug, do not catch this')
            f = open(f"{fileName}.txt", "r")
            f.close()
            f = open(f"{fileName}.txt", "a")
            content = input("New info: ")
            f.write(f"{content}")
            b = False
        except ValueError:
            print("Please enter valid file name")
        except FileNotFoundError:
            print(f"File named '{fileName}' doesn't exist")
        except Exception as e:
            print(f"{e}")
        else:
            print("File is successfully updated!")
        finally:
            f.close()
            print("File has been closed!")