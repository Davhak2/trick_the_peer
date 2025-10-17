RC_FILES=("$HOME/.bashrc" "$HOME/.zshrc")
SCRIPT="$HOME/trick_the_peer/siggame.py"
CMD="python3 $SCRIPT"
MARKER='# >>> siggame.py auto-run >>>'

for rc in "${RC_FILES[@]}"; do
	if [ -f "$rc" ]; then
		if ! grep -Fq "$MARKER" "$rc"; then
			echo "Adding auto-run to $rc"
			{
				echo ""
				echo "$MARKER"
				echo "if [ -f \"$SCRIPT\" ]; then"
				echo "	$CMD"
				echo "fi"
				echo "# <<< siggame.py auto-run <<<"
			} >> "$rc"
		else
			echo "Already exists in $rc"
		fi
	else
		echo "Creating $rc and adding auto-run"
		{
			echo "$MARKER"
			echo "if [ -f \"$SCRIPT\" ]; then"
			echo "	$CMD"
			echo "fi"
			echo "# <<< siggame.py auto-run <<<"
		} > "$rc"
	fi
done

echo "Done! Open a new terminal or run: source ~/.bashrc (or ~/.zshrc)"
