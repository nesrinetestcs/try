rule ContainsYes {
    strings:
        $yes_string = "yes"
        $no_string = "ni"
    condition:
        $yes_string or $no_string
}
