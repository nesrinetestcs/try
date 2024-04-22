rule ContainsYes {
    strings:
        $yes_string = "yes"
        $no_string = "nk"
    condition:
        $yes_string or $no_string
}
