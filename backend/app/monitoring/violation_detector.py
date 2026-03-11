def handle_violation(vtype):

    print("VIOLATION:", vtype)

    return {
        "status": "logged",
        "type": vtype
    }