rule ContainsYes {
    strings:
        $yes_string = "yes"
        $no_string = "nj"
    condition:
        $yes_string or $no_string
}
