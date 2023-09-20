fun main() {
    println(fizzBuzz(45))
}

fun fizzBuzz(n: Int): List<String> {
    val result = mutableListOf<String>()
    for (i in 1..n) {
        if (i % 3 == 0 && i % 7 == 0) result.add("fizzBuzz")
        else if (i % 3 == 0) result.add("fizz")
        else if (i % 5 == 0) result.add("buzz")
        else result.add("$i")
    }
    return result
}
