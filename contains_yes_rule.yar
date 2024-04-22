rule ContainsYes {
    strings:
        $yes_str  ing = "yes"

    condition:
        $yes_string
}
