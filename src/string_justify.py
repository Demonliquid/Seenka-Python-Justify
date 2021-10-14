def Justify(string: str, maxWidth: int) -> str:
    """Returns justified string.

    Keyword args:
    string -- string largo para que se note
    maxWidth -- ancho del texto final

    Use:
    print(Justify(string, maxWidth))
    """
    words = string.split()
    res, cur, num_of_letters = [], [], 0
    for w in words:
        # El condicional revisa que cada palabra entre en las columnas permitidas
        assert (  # No me gusta el formato de este assert, pero black me lo bloquea
            len(w) < maxWidth
        ), "Error: La palabra mas larga no entra en las columnas asignadas"
        # El condicional revisa que haya espacio en el renglon
        if num_of_letters + len(w) + len(cur) > maxWidth:
            for i in range(maxWidth - num_of_letters):
                cur[i % (len(cur) - 1 or 1)] += " "
            res.append("".join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    return "\n".join(res + [" ".join(cur).ljust(maxWidth)])
