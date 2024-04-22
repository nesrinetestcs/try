rule ContainsYes {
    strings:
        $yes_string = "yes"
        $nk_string = "nk"
    condition:
        $yes_string or $nk_string
}
