{ pkgs ? import <nixpkgs> {} }:

pkgs.python3Packages.buildPythonApplication {
  pname = "mvd";
  version = "0.1.0";

  src = ./.;

  # No additional dependencies are required as the script uses only Python's standard library
  propagatedBuildInputs = [];

  # Skip the standard build and check phases since there is no setup.py
  buildPhase = "true";
  checkPhase = "true";

  # Set format to "other" to avoid dist output check
  format = "other";

  # Custom install phase to copy main.py to the output bin directory
  installPhase = ''
    mkdir -p $out/bin
    cp main.py $out/bin/mvd
    chmod +x $out/bin/mvd
  '';

  # Optional metadata
  meta = with pkgs.lib; {
    description = "A Python script to move and rename files from the Downloads folder based on custom criteria.";
    homepage = "https://github.com/MrZeLee/mvd";
    maintainers = with maintainers; [ MrZeLee ];
  };
}
