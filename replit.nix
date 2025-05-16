
{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.flask
    pkgs.python311Packages.openai
    pkgs.python311Packages.flask_cors
  ];
}
