# Trick the Peer 🎯

A challenging terminal-based puzzle game that tests your problem-solving skills!

## 🚀 Installation & Setup

Follow these steps to install and run the game:

### 1. Navigate to Home Directory
```bash
cd ~
```

### 2. Clone the Repository
```bash
git clone https://github.com/Davhak2/trick_the_peer.git
```

### 3. Enter the Repository Directory
```bash
cd trick_the_peer
```

### 4. Make the Script Executable and Run It
```bash
chmod +x install.sh
./install.sh
```

### 5. Source Your RC File
After completing the challenge, remember to clean up:
```bash
# For bash users
source ~/.bashrc

# For zsh users
source ~/.zshrc
```

## 🎯 Objective

Your goal is to discover the secret phrase and successfully exit the program. The game responds to:
- Regular keyboard input
- Signal combinations (Ctrl+C, Ctrl+Z, etc.)
- Specific attempt thresholds that reveal hints

## ⚠️ Important Notes

- The game includes a lockout mechanism after multiple failed attempts
- Different messages appear based on your progress
- Pay close attention to the hints - they contain valuable information!
- Remember to clean up the script from your shell configuration after completing

## 🏆 Victory

Once you successfully discover the secret phrase, follow the instructions to remove the script runner from your shell configuration file.

---

**Good luck, and may your persistence be rewarded! 🍀**
