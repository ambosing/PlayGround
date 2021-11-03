import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JMenuBar;

@SuppressWarnings("serial")
public class KoreaChess extends Information {
	final int NULL = 0;
	final int BUSH = 4;

	final int pho = 3;
	final int sang = 5;
	final int sa = 6;
	final int jol = 7;

	final int Rpho = 10;
	final int Rsang = 12;
	final int Rsa = 13;
	final int Rjol = 14;

	static int myTurn = 0;
	boolean start = false;
	boolean janggun = false;
	Information information;
	CheckStart check;

	JFrame mainFrame;
	JPanel panel = new JPanel();
	JPanel gameZone = new JPanel() {
		public void paintComponent(Graphics g) {
			g.drawImage(icon.getImage(), 0, 0, 770, getHeight(), null);
			setOpaque(false);
			super.paintComponent(g);
		}
	};
	ImageIcon icon;
	GameMenu menu;
	CheckMove checkmove = new CheckMove();
	int[][] janggiBoard;
	int[] malIndex, malIndextmp;

	public KoreaChess() {

		mainFrame = new JFrame();
		mainFrame.setTitle("Bugs War"); // 제목 바꿔야함
		mainFrame.setLayout(null);
		mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		information = new Information();
		icon = new ImageIcon("images/board.jpg"); // 판 바꿀때 이것만 바꾸면 됩니당.
		menu = new GameMenu();
		check = new CheckStart();

		panel.setLayout(null);
		gameZone.setLayout(null);
		janggiBoard = init();
		gameZone = Locate(janggiBoard, gameZone);
		panel.add(gameZone);
		panel.add(information);
		check.start();

		gameZone.setSize(800, 966);
		mainFrame.setJMenuBar(menu);
		mainFrame.setContentPane(panel);
		mainFrame.setBounds(500, 5, 1000, 1020/* 760 */);
		mainFrame.setResizable(false);
		mainFrame.setVisible(true);

		scbar1 = new JLabel(score1.toString());
		scbar1.setFont(new Font("맑은고딕", Font.BOLD, 60));
		PlayerPanel[0].removeAll();
		PlayerPanel[0].add(scbar1);
		scbar2 = new JLabel(score2.toString());
		scbar2.setFont(new Font("맑은고딕", Font.BOLD, 60));
		PlayerPanel[1].removeAll();
		PlayerPanel[1].add(scbar2);

		// repeatSound.wakeup();
	}

	class CheckStart extends Thread {
		int count = 0;

		public void run() {
			// while (true) {
			while (true) {
				if (!information.IsStart && count == 0) {
					janggiBoard = init();
					gameZone.removeAll();
					gameZone = Locate(janggiBoard, gameZone);
					gameZone.repaint();
					myTurn = 0;
					information.Player[0].setSelected(true);
					information.Player[1].setSelected(false);
					count++;
				} 
				else if (information.IsStart && count != 0) {
					count = 0;
				}
			}
		}
	}

	public class mal extends JButton {
		int x;
		int y;
		ImageIcon icon;

		public mal(int i, int j, String imagePath) {
			setSize(60, 60);
			setLocation((i * 61 + 19), (j * 58 + 18)); // 말 사이의 간격 조정
			icon = new ImageIcon(imagePath);

			addMouseListener(new MouseListener() {

				@Override
				public void mouseReleased(MouseEvent e) {
					// TODO Auto-generated method stub
					if (information.IsStart) {

						JButton btn = (JButton) e.getSource();
						btn.setSelected(false);
						x = e.getXOnScreen() - mainFrame.getX();
						y = e.getYOnScreen() - mainFrame.getY() - 30;
						System.out.println(x + "  " + y);
						malIndex = getIndex(x, y);
						System.out.println(malIndex[0] + "  " + malIndex[1]);
						System.out.println(janggiBoard[malIndextmp[0]][malIndextmp[1]]);
						System.out.println(myTurn);
						if (janggiBoard[malIndextmp[0]][malIndextmp[1]] / 8 == myTurn) {
							if (malIndex[0] == malIndextmp[0] && malIndextmp[1] == malIndex[1])
								;
							else if (checkmove.CheackMalMove( // board[][], i ,
																// pre, now
									janggiBoard, janggiBoard[malIndextmp[0]][malIndextmp[1]], malIndextmp, malIndex)) {
								if (janggiBoard[malIndex[0]][malIndex[1]] == NULL) {
									janggiBoard[malIndex[0]][malIndex[1]] = janggiBoard[malIndextmp[0]][malIndextmp[1]];
									janggiBoard[malIndextmp[0]][malIndextmp[1]] = NULL;
									// moveSound.wakeup();
									setChangeTurn();
								} else if (janggiBoard[malIndex[0]][malIndex[1]]
										/ 8 == janggiBoard[malIndextmp[0]][malIndextmp[1]] / 8)
									;
								else if (janggiBoard[malIndex[0]][malIndex[1]] % 7 == 3
										&& janggiBoard[malIndextmp[0]][malIndextmp[1]] % 7 == 3)
									;
								else { // 왕이 말에게 잡혀서 게임이 끝났을 때 우리는 스코어가 12점이 됬을때
										// 게임이 끝났습니다 나오고 종료되게 만들어야함.
									if (myTurn == 0 && information.score1 == 12) {
										start = false;
										JOptionPane.showConfirmDialog(null, "총 스코어 12점!", "파란팀이 이겼습니다.",
												JOptionPane.WARNING_MESSAGE);
										information.IsStart = false;
										information.ResetTimer();
										information.IsStart = false;
										information.PlayerPanel[0].removeAll();
										information.PlayerPanel[1].removeAll();
									} else {
										information.setPlayerEatMal(janggiBoard[malIndex[0]][malIndex[1]], malIndex[0],
												malIndex[1]);
										janggiBoard[malIndex[0]][malIndex[1]] = janggiBoard[malIndextmp[0]][malIndextmp[1]];
										janggiBoard[malIndextmp[0]][malIndextmp[1]] = NULL;
										setChangeTurn();
									}
								}
							}
						}

						btn.setLocation(checkPlace(x, y));
						gameZone.removeAll();
						gameZone = Locate(janggiBoard, gameZone);
						gameZone.repaint();
						Rint(janggiBoard);
						System.out.println("");
					}

				}

				@Override
				public void mousePressed(MouseEvent e) {
					// TODO Auto-generated method stub
					JButton btn = (JButton) e.getSource();
					btn.setSelected(false);
					x = e.getXOnScreen() - mainFrame.getX();
					y = e.getYOnScreen() - mainFrame.getY() - 30;
					malIndextmp = getIndex(x, y);
					System.out.println(malIndextmp[0] + "  " + malIndextmp[1]);
					information.DisplayMove(janggiBoard[malIndextmp[0]][malIndextmp[1]]);
				}

				@Override
				public void mouseExited(MouseEvent arg0) {
					// TODO Auto-generated method stub

				}

				@Override
				public void mouseEntered(MouseEvent arg0) {
					// TODO Auto-generated method stub

				}

				@Override
				public void mouseClicked(MouseEvent e) {
					// TODO Auto-generated method stub
				}
			});

			addMouseMotionListener(new MouseMotionListener() {

				@Override
				public void mouseDragged(MouseEvent e) {
					// TODO Auto-generated method stub
					if (information.IsStart) {
						JButton btn = (JButton) e.getSource();
						x = e.getXOnScreen() - mainFrame.getX();
						y = e.getYOnScreen() - mainFrame.getY();
						if (x < 810 && x > 10 && y < 1000 && y > 10)
							btn.setLocation(x - 35, y - 80);
					}

				}

				@Override
				public void mouseMoved(MouseEvent arg0) {
					// TODO Auto-generated method stub

				}
			});
		}

		public void paintComponent(Graphics g) { // 말의 크기를 조정
			g.drawImage(icon.getImage(), 0, 0, 60, 60, null);
			setOpaque(false);
		}
	}

	public int[] getIndex(int ox, int oy) {
		int[] Index = new int[2];
		Point tmp = new Point();
		for (int i = 0; i < 12; i++) {
			for (int j = 0; j < 16; j++) {
				if ((tmp.x - ox) * (tmp.x - ox)
						+ (tmp.y - oy) * (tmp.y - oy) > (((i + 1) * 60 + 27) - ox) * (((i + 1) * 60 + 27) - ox)
								+ (((j + 1) * 59 + 28) - oy) * (((j + 1) * 59 + 28) - oy)) {
					tmp.setLocation(i * 60 + 27, j * 59 + 28); // 처음 말 크기 계산이
																// 72+20이였다.
					Index[0] = i;
					Index[1] = j;
				}
			}
		}

		return Index; // 크기가 크다면 그 i j 값을 인덱스 배열에 넣어서 반환한다.
	}

	public Point checkPlace(int ox, int oy) {
		Point Place = new Point();
		Point tmp = new Point();
		for (int i = 0; i < 12; i++) {
			for (int j = 0; j < 16; j++) {
				if ((tmp.x - ox) * (tmp.x - ox)
						+ (tmp.y - oy) * (tmp.y - oy) > (((i + 1) * 60 + 27) - ox) * (((i + 1) * 60 + 27) - ox)
								+ (((j + 1) * 59 + 28) - oy) * (((j + 1) * 59 + 28) - oy)) {
					tmp.setLocation(i * 60 + 27, j * 59 + 28); // 처음 말 크기가 72+20
																// 이였다
				}
			}
		}
		Place.setLocation(tmp.getLocation());

		return Place;
	}

	public void Rint(int[][] janggiBoard) {

		for (int i = 0; i < 12; i++) {
			for (int j = 0; j < 16; j++) {
				System.out.print(" " + janggiBoard[i][j] + " ");
			}
			System.out.println("");
		}
	}

	public int[][] init() {

		int[][] Janggipan = {
				{ NULL, NULL, NULL, NULL, NULL, jol, NULL, NULL, NULL, NULL, Rjol, NULL, NULL, NULL, NULL, NULL },
				{ NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL },
				{ NULL, NULL, NULL, sang, NULL, BUSH, NULL, NULL, NULL, NULL, BUSH, NULL, Rsang, NULL, NULL, NULL },
				{ pho, sa, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, Rsa, Rpho },
				{ NULL, NULL, NULL, sang, NULL, jol, NULL, NULL, NULL, NULL, Rjol, NULL, Rsang, NULL, NULL, NULL },
				{ NULL, NULL, BUSH, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, },
				{ NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, BUSH, NULL, NULL, },
				{ NULL, NULL, NULL, sang, NULL, jol, NULL, NULL, NULL, NULL, Rjol, NULL, Rsang, NULL, NULL, NULL },
				{ pho, sa, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, Rsa, Rpho },
				{ NULL, NULL, NULL, sang, NULL, BUSH, NULL, NULL, NULL, NULL, BUSH, NULL, Rsang, NULL, NULL, NULL },
				{ NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL },
				{ NULL, NULL, NULL, NULL, NULL, jol, NULL, NULL, NULL, NULL, Rjol, NULL, NULL, NULL, NULL, NULL },

		};

		return Janggipan;
	}

	public JPanel Locate(int[][] board, JPanel Janggi) {

		for (int i = 0; i < 12; i++) {
			for (int j = 0; j < 16; j++) {
				if (board[i][j] == pho) {
					mal Ppho = new mal(i, j, "images/po.jpg");
					Ppho.setBackground(Color.GREEN);
					Ppho.setName("images/po.jpg");
					Janggi.add(Ppho);
				} else if (board[i][j] == sang) {
					mal Psang = new mal(i, j, "images/sang.jpg");
					Psang.setBackground(Color.GREEN);
					Psang.setName("images/sang.jpg");
					Janggi.add(Psang);
				} else if (board[i][j] == sa) {
					mal Psa = new mal(i, j, "images/sa.jpg");
					Psa.setBackground(Color.GREEN);
					Psa.setName("images/sa.jpg");
					Janggi.add(Psa);
				} else if (board[i][j] == jol) {
					mal Pjol = new mal(i, j, "images/jol.jpg");
					Pjol.setBackground(Color.GREEN);
					Pjol.setName("images/jol.jpg");
					Janggi.add(Pjol);
				} else if (board[i][j] == Rpho) {
					mal Rpho = new mal(i, j, "images/rpo.jpg");
					Rpho.setBackground(Color.RED);
					Rpho.setName("images/rpo.jpg");
					Janggi.add(Rpho);
				} else if (board[i][j] == Rsang) {
					mal Rsang = new mal(i, j, "images/rsang.jpg");
					Rsang.setBackground(Color.RED);
					Rsang.setName("images/rsang.jpg");
					Janggi.add(Rsang);
				} else if (board[i][j] == Rsa) {
					mal Rsa = new mal(i, j, "images/rsa.jpg");
					Rsa.setBackground(Color.RED);
					Rsa.setName("images/rsa.jpg");
					Janggi.add(Rsa);
				} else if (board[i][j] == Rjol) {
					mal Rjol = new mal(i, j, "images/rjol.png");
					Rjol.setBackground(Color.RED);
					Rjol.setName("images/rjol.png");
					Janggi.add(Rjol);
				}
			}
		}

		return Janggi;
	}

	public static void changeTurn() {
		if (myTurn == 0) {
			myTurn = 1;
		} else {
			myTurn = 0;
		}
	}

	/**
	 * @param args
	 */

	public void setChangeTurn() {
		if (myTurn == 0) {
			myTurn = 1;
			information.setTurnIsChangeToTrue();
		} else {
			myTurn = 0;
			information.setTurnIsChangeToTrue();
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new KoreaChess();
	}
}
