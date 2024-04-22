rule ContainsYes {
    strings:
        $yes_string = "yes"
        $no_string = "no"
    condition:
        $yes_string or $no_string
}
