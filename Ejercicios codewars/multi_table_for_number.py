def multi_table(multiplicando):
    tabla_de_multiplicar = ""

    for multiplicador in range(1, 11):
        if multiplicador == 10:
            tabla_de_multiplicar += f"{multiplicador} * {multiplicando} = {multiplicador * multiplicando}"
        else:
            tabla_de_multiplicar += f"{multiplicador} * {multiplicando} = {multiplicador * multiplicando}\n"

    return tabla_de_multiplicar



Scala 



def multiTable(n: Int): String = {
var multiplo = 1
var table: String=("")
while multiplo<10 do
  table+=(s"$multiplo * $n = " + multiplo * n+"\n")
  multiplo=multiplo+1
 table+=(s"$multiplo * $n = " + multiplo * n)
return(table)
}
