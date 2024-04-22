rule ContainsYes {
    strings:
        $yes_string = "yes"
        $nk_string = "no"
    condition:
        $yes_string or $nk_string
}
