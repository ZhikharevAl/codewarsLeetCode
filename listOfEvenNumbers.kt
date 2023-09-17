fun main() {
    val listOfNumbers = mutableListOf<Int>()
    for (i in 1..99) {
        listOfNumbers.add(i)
    }
    val listOfEvenNumbers = listOfNumbers.filter { it % 2 == 0 }
    for (number in listOfEvenNumbers) {
        println(number)
    }
}
