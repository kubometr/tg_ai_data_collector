{ pkgs }: {
  deps = [
    pkgs.python39Full  # или твоя версия Python
    pkgs.antiword     # вот он — antiword
    # остальные зависимости
  ];
}
