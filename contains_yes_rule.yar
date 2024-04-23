rule ContainsYes {
    strings:
        $yes_string = "yes"
        $no_string = "n"
    condition:
        $yes_string or $no_string
}
