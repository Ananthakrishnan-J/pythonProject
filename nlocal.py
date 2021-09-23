def outer_fun():
    d = "d from the outer function"

    def inner_fun():
        d = "d from the inner function"
        print(d)

    print(d)
    inner_fun()

outer_fun()
