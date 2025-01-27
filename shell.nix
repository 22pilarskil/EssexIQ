{ pkgs ? import <nixpkgs> {} }:
(pkgs.buildFHSUserEnv {
  name = "pipzone";
  targetPkgs = pkgs: (with pkgs; [
    python314
    python314Packages.pip
    python314Packages.virtualenv
  ]);
  runScript = "bash";
}).env

