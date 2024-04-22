rule ContainsYes {
    strings:
        $yes_string = "yes"
  nnn
    condition:
        $yes_string
}
