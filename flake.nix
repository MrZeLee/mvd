{
  description = "A flake for the mvd package";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs";

  outputs = { self, nixpkgs }: {
    packages = {
      # Define the package for each system
      default = system:
        let
          pkgs = import nixpkgs { inherit system; };
        in
          pkgs.callPackage ./default.nix {};
    };
  };
}
