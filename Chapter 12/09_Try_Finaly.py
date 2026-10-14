# TRY WITH FINALLY

# Python offers a ‘finally’ clause which ensures execution of a piece of code inspective of the exception.
def main():
    try:
        a = int(input("Enter a numbeer"))
        print(a)
        return


    except Exception as e:
        print(e)
        return


    finally:
        print("Hey i am inside of finaly")

main()

# finaly sirf function me hi kam aata hain
# otherwise ham print bhi kr sakte hain
# finaly block chalta hi hain
