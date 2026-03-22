[[ -f "$HOME/.zshrc" ]] && source "$HOME/.zshrc"

if [[ -z "${VIRTUAL_ENV:-}" ]]; then
  dir="$PWD"
  while [[ "$dir" != "/" ]]; do
    if [[ -f "$dir/.venv/bin/activate" ]]; then
      source "$dir/.venv/bin/activate"
      break
    fi
    dir="${dir:h}"
  done
fi

function _trae_ensure_venv_path() {
  if [[ -n "${VIRTUAL_ENV:-}" ]]; then
    case ":$PATH:" in
      *":$VIRTUAL_ENV/bin:"*) ;;
      *) export PATH="$VIRTUAL_ENV/bin:$PATH" ;;
    esac
    hash -r 2>/dev/null || true
  fi
}

typeset -ga precmd_functions
precmd_functions+=(_trae_ensure_venv_path)
_trae_ensure_venv_path
