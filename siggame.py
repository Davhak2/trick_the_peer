import signal
import sys
import os
import time
import threading

class Trick:
	def __init__(self):
		self.secret = "ElKompsBacChemToxni"
		self.attempts = 0
		self.lernik = 0
		self.locked_until = 0
		self.signal_attempts = 0
		self.passwrd = False
		self.flag = False
		self.hide_prompt = False
		self.enter = False
		self.signals = {
			signal.SIGINT,
			signal.SIGQUIT,
			signal.SIGTSTP,
			signal.SIGTERM,
			signal.SIGHUP,
			signal.SIGUSR1,
			signal.SIGUSR2,
		}

		for sig in self.signals:
			try:
				signal.signal(sig, self.handler)
			except (OSError, RuntimeError, ValueError):
				pass

	def handler(self, signum, frame):
		if time.time() < self.locked_until:
			print("\033[91m⏳ Locked! Please wait...\033[0m")
			return
		self.signal_attempts += 1
		self.clear_tab()

	def clear_tab(self, show_message=True):
		os.system('clear' if os.name == 'posix' else 'cls')
		effective_show = show_message and not self.hide_prompt and not self.enter and self.attempts != 5
		if self.hide_prompt:
			self.hide_prompt = False
		if self.enter:
			self.enter = False
		if effective_show:
			if self.signal_attempts == 242:
				print("\033[34m" + "Eeee de hmi uzac chuzac nuyn krugy pti fras" + "\033[0m")
				self.signal_attempts = 0
			elif self.signal_attempts > 230:
				print("\033[34m" + f"Hargelis password-y \"{self.secret}\" a" + "\033[0m")
			elif self.signal_attempts >= 225 and self.signal_attempts <= 230:
				print("\033[34m" + f"Password-y \"{self.secret}\" a" + "\033[0m")
			elif self.signal_attempts % 50 == 0:
				print("\033[34m" + "Ara de asum em eli anasun erkir a" + "\033[0m")
			elif self.signal_attempts % 15 == 0:
				print("\033[34m" +"Ba urish vonc es ape?" + "\033[0m")
			elif self.signal_attempts % 11 == 0:
				print("\033[34m" +"Axjkeq jan vor hasneq 500 drami indzi dzen ktaq" + "\033[0m")
			elif self.signal_attempts % 5 == 0:
				print("\033[34m" + "Vay es el gitei qez ruchken a petq" + "\033[0m")
			else:
				print("\033[34m" + "Ujex qashi" + "\033[0m")

	def mission_success(self):
		self.clear_tab(show_message=False)
		print("\033[92m🎉 Congratulations! You discovered the secret phrase.\033[0m")
		print("\033[93m\n\n\nCAUTION!!!\033[0m")
		print("\033[96mPlease remove the script runner command from the ~/.zshrc or ~/.bashrc file and enjoy coding! 😎\033[0m")
		print("\033[95mBest Regards, Davihako\033[0m")
		print("\033[94m\n\nGithub:   Davhak2\033[0m")
		print("\033[96mTelegram: @ICantGetNoW\033[0m")
		sys.exit(0)

	def lockout(self):
		self.locked_until = time.time() + 30
		self.clear_tab()
		print("\033[91m⏳ Too many attempts! Locked for 30 seconds...\033[0m")
		while time.time() < self.locked_until:
			time.sleep(1)
		self.attempts = 0
		self.clear_tab(show_message=False)
		print("\033[92m✅ You can try again now.\033[0m")

	def default_loop(self):
		while True:
			if time.time() >= self.locked_until and not self.passwrd:
				print("\033[33m" + "la" + "\033[0m", end="", flush=True)
			time.sleep(0.08)

	def run(self):
		print("\033[95mWelcome to the program, Qashvar!!!\nTry to exit from here\033[0m")

		dfl = threading.Thread(target=self.default_loop, daemon=True)
		dfl.start()
		while True:
			try:
				if time.time() < self.locked_until:
					print("\033[91m⏳ Locked! Please wait...\033[0m")
					time.sleep(1)
					continue
				line = input("").strip()
				self.enter = True
				self.clear_tab()
				if self.lernik % 3 == 0:
					print("\033[91mLERNIK IN REEED\033[0m")
				elif self.lernik % 3 == 1:
					print("\033[93mIS RISING FOR MEEEE\033[0m")
				else:
					print("\033[92mOH YEAAAAH...\033[0m")
				self.lernik += 1
			except EOFError:
				if time.time() < self.locked_until:
					print("\033[91m⏳ Locked! Please wait...\033[0m")
					time.sleep(1)
					continue
				print("\033[31m\nDavay de paroly asa\033[0m")
				self.passwrd = True
				try:
					password = input("").strip()
					if password == self.secret:
						self.mission_success()
					else:
						self.hide_prompt = True
						self.clear_tab()
						print("\033[1mChkpav ynger jan\033[0m")
						self.attempts += 1
						print(f"\033[31mAttempts left: {5 - self.attempts}\033[0m")
						if self.attempts % 5 == 0:
							self.lockout()
				except (EOFError, KeyboardInterrupt):
					self.clear_tab(show_message=False)
				finally:
					self.passwrd = False
			except KeyboardInterrupt:
				if time.time() < self.locked_until:
					print("\033[91m⏳ Locked! Please wait...\033[0m")
					time.sleep(1)
					continue
				self.clear_tab()

if __name__ == "__main__":
	Trick().run()
