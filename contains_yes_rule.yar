rule ContainsYes {
    strings:
        $yes_string = "yes"
     
    condition:
        $yes_string
}
