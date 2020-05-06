{ pkgs ? import <nixpkgs> {} }:

with pkgs;

mkShell {
  buildInputs = [
    entr
    (python3.withPackages (ps: with ps; [
      black
      python-language-server
      ipython
      yattag
    ]))
  ];
}
