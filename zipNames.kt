fun main() {
    val names: MutableList<String> = mutableListOf<String>()
    val phones: MutableList<Long> = mutableListOf<Long>()
    for (i in 0..1000) {
        names.add("Имя$i")
        phones.add(79_000_000_000 + i.toLong())
    }
    val users = names.zip(phones)
    for (user in users) {
        println("Имя ${user.first} Телефон ${user.second}")
    }
}
