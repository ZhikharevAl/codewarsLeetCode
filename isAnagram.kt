fun isAnagram(s: String, t: String): Boolean {
        return s.toCharArray().sorted() == t.toCharArray().sorted()
    }
