import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.io.File;

import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.DataLine;
import javax.sound.sampled.SourceDataLine;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JToggleButton;
import javax.swing.SwingConstants;
import javax.swing.border.LineBorder;
import javax.swing.border.TitledBorder;

@SuppressWarnings("serial")
public class Information extends JPanel {
	JLabel RemainTime, PlayTime;
	JButton Startbu;
	JButton Endbu;
	JPanel jp2;
	JPanel display;
	JButton HansuBack;
	JToggleButton[] Player;
	PlayTimer PlayTimer;
	RemainTimer RemainTimer;
	public static JPanel[] PlayerPanel;
	int hours, mins, secs, hours1, mins1, secs1;
	double oo, xx, oo1, xx1;
	boolean loop, first = true, TurnIsChange = false;
	ImageIcon icon;
	public static Integer score1 = 0;
	public static Integer score2 = 0;
	public static JLabel scbar1;
	public static JLabel scbar2;
	JPanel turnColor = new JPanel();

	boolean IsStart;

	void setTurnIsChangeToTrue() {// TurnIsChange�� True�� ����.���̹ٲ�� �����ð� �ʱ�ȭ�� ���ؼ�
		TurnIsChange = true;
		SetTurn();
	}

	void SetTurn() {// ���� �ٲ�� ��۹�ư�� �ٲ��
		if (Player[0].isSelected()) {
			Player[0].setSelected(false);
			Player[1].setSelected(true);
			turnColor.setBackground(Color.RED);
		} else {
			Player[1].setSelected(false);
			Player[0].setSelected(true);
			turnColor.setBackground(Color.BLUE);
		}
	}

	public void ResetTimer() {
		RemainTime.setText("00:00:00");
		HansuBack.setVisible(false);
		Startbu.setVisible(true);
		PlayTimer.suspend();
		RemainTimer.suspend();
		IsStart = false;
	}
	
 
 
 
 public void play(){
	    try {
	      File soundFile = new File("Music/LDie.wav");  // File �� �ޱ�
	      AudioInputStream audioInputStream = AudioSystem.getAudioInputStream(soundFile);
	      // �޾ƿ� File ������ ����� �Է� ��Ʈ���� ��ȯ��, ��Ÿ�� ���ڵ��� ����� �Է� ��Ʈ���� ��� 
	      
	      AudioFormat audioFormat = audioInputStream.getFormat();
	      // ����Ʈ���� �ƴϰ� ���� �����Ӽ��� ��Ÿ������, ��Ʈ���� ���̸� ���

	      DataLine.Info info = new DataLine.Info(SourceDataLine.class,audioFormat);
	      // ������ ����� ������ ������ ������ �����κ��� ������ ������ ���� ������Ʈ�� ����

	      SourceDataLine line = (SourceDataLine) AudioSystem.getLine(info);
	      // ������ Line.Info ������Ʈ�� ����� ��ġ�ϴ� ������ ���

	      line.open(audioFormat);
	     // ������ ���İ� ������ ���� ������� ������ ����, ������ �ʿ��� system resource�� ȹ���� ���� ����
	      line.start();
	    // ���ο����� ������ ������� ����

	      int nBytesRead = 0;
	      byte[] abData = new byte[128000];
	      while (nBytesRead != -1) {
	        nBytesRead = audioInputStream.read(abData, 0, abData.length);
	        if (nBytesRead >= 0) {
	          int nBytesWritten = line.write(abData, 0, nBytesRead);
	        }
	      }
	    }
	 catch (Exception e) {
	      e.printStackTrace();
	    }
	  }
 public void startplay(){
	    try {
	      File startFile = new File("Music/1-Up.wav");  // File �� �ޱ�
	      AudioInputStream startInputStream = AudioSystem.getAudioInputStream(startFile);
	      // �޾ƿ� File ������ ����� �Է� ��Ʈ���� ��ȯ��, ��Ÿ�� ���ڵ��� ����� �Է� ��Ʈ���� ��� 
	      
	      AudioFormat startFormat = startInputStream.getFormat();
	      // ����Ʈ���� �ƴϰ� ���� �����Ӽ��� ��Ÿ������, ��Ʈ���� ���̸� ���

	      DataLine.Info startinfo = new DataLine.Info(SourceDataLine.class,startFormat);
	      // ������ ����� ������ ������ ������ �����κ��� ������ ������ ���� ������Ʈ�� ����

	      SourceDataLine startline = (SourceDataLine) AudioSystem.getLine(startinfo);
	      // ������ Line.Info ������Ʈ�� ����� ��ġ�ϴ� ������ ���

	      startline.open(startFormat);
	     // ������ ���İ� ������ ���� ������� ������ ����, ������ �ʿ��� system resource�� ȹ���� ���� ����
	      startline.start();
	    // ���ο����� ������ ������� ����

	      int nBytesRead = 0;
	      byte[] abData = new byte[128000];
	      while (nBytesRead != -1) {
	        nBytesRead = startInputStream.read(abData, 0, abData.length);
	        if (nBytesRead >= 0) {
	          int nBytesWritten = startline.write(abData, 0, nBytesRead);
	        }
	      }
	    }
	 catch (Exception e) {
	      e.printStackTrace();
	    }
	  }
 
 public void endplay(){
	    try {
	     // File �� �ޱ�
	      File ending = new File("Music/ending.wav");
	      // �޾ƿ� File ������ ����� �Է� ��Ʈ���� ��ȯ��, ��Ÿ�� ���ڵ��� ����� �Է� ��Ʈ���� ��� 
	      AudioInputStream endInputStream = AudioSystem.getAudioInputStream(ending);
	      
	      AudioFormat endFormat = endInputStream.getFormat();
	      // ����Ʈ���� �ƴϰ� ���� �����Ӽ��� ��Ÿ������, ��Ʈ���� ���̸� ���

	      // ������ ����� ������ ������ ������ �����κ��� ������ ������ ���� ������Ʈ�� ����
	      DataLine.Info endinfo = new DataLine.Info(SourceDataLine.class,endFormat);

	      SourceDataLine endline = (SourceDataLine) AudioSystem.getLine(endinfo);
	      // ������ Line.Info ������Ʈ�� ����� ��ġ�ϴ� ������ ���

	     // ������ ���İ� ������ ���� ������� ������ ����, ������ �ʿ��� system resource�� ȹ���� ���� ����
	      endline.open(endFormat);
	    // ���ο����� ������ ������� ����
	      endline.start();

	      int nBytesRead = 0;
	      byte[] abData = new byte[128000];
	      while (nBytesRead != -1) {
	        nBytesRead = endInputStream.read(abData, 0, abData.length);
	        if (nBytesRead >= 0) {
	          int nBytesWritten = endline.write(abData, 0, nBytesRead);
	        }
	      }
	    }
	 catch (Exception e) {
	      e.printStackTrace();
	    }
	  }
 

	void setPlayerEatMal(int killedMal, int x, int y) {
		// ���� �ε�����, ���� ���� �ε����� x��ǥ��, y��ǥ�� �Ű������� �޾� �����ϴ� �Լ�
		play(); //���� �������� ��� ������ �Ҹ� ����
		aa: { // ���� ĵ�������� �������� �׷��� ���������� ������ �� ���� ����ϴ� �Լ�.
			if ((killedMal == 3) && ((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// �������� �ε����� 3(�Ķ�ǳ����)�̰� x,y�� ��ǥ�� �ν����̶�� ������ ���ھ� +3, ����� ���ھ� -6�� ���ش�.
				score2 += 3;
				score1 -= 6;
				break aa;
			}

			if (killedMal == 3 && !((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// �������� �ε����� 3(�Ķ�ǳ����)�̰� x,y�� ��ǥ�� �ν����� �ƴ϶�� ������ ���ھ� +3�� ���ش�.
				score2 += 3;
				break aa;
			}

			if (killedMal == 5 && ((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// �������� �ε����� 5(�Ķ��Ź�)�̰� x,y�� ��ǥ�� �ν����̶�� ������ ���ھ� +2, ����� ���ھ� -4�� ���ش�.
				score2 += 2;
				score1 -= 4;
				break aa;
			}

			if (killedMal == 5 && !((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// �������� �ε����� 5(�Ķ��Ź�)�̰� x,y�� ��ǥ�� �ν����� �ƴ϶�� ������ ���ھ� +2�� ���ش�.
				score2 += 2;
				break aa;
			}

			if (killedMal == 6 && ((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// �������� �ε����� 6(�Ķ��ֹ���)�̰� x,y�� ��ǥ�� �ν����̶�� ������ ���ھ� +4, ����� ���ھ� -8�� ���ش�.
				score2 += 4;
				score1 -= 8;
				break aa;
			}

			if (killedMal == 6 && !((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// �������� �ε����� 6(�Ķ��ֹ���)�̰� x,y�� ��ǥ�� �ν����� �ƴ϶�� ������ ���ھ� +4�� ���ش�.
				score2 += 4;
				break aa;

			}

			if (killedMal == 7 && ((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// �������� �ε����� 7(�Ķ�����)�̰� x,y�� ��ǥ�� �ν����̶�� ������ ���ھ� +1, ����� ���ھ� -2�� ���ش�.
				score2 += 1;
				score1 -= 2;
				break aa;
			}

			if (killedMal == 7 && !((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// �������� �ε����� 7(�Ķ�����)�̰� x,y�� ��ǥ�� �ν����� �ƴ϶�� ������ ���ھ� +1�� ���ش�.
				score2 += 1;
				break aa;
			}

			if (killedMal == 10 && ((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// �������� �ε����� 10(����ǳ����)�̰� x,y�� ��ǥ�� �ν����̶�� ����� ���ھ� +3, ������ ���ھ� -6�� ���ش�.
				score1 += 3;
				score2 -= 6;
				break aa;
			}

			if (killedMal == 10 && !((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// �������� �ε����� 10(����ǳ����)�̰� x,y�� ��ǥ�� �ν����� �ƴ϶�� ����� ���ھ� +3�� ���ش�.
				score1 += 3;
				break aa;
			}

			if (killedMal == 12 && ((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// �������� �ε����� 12(�����Ź�)�̰� x,y�� ��ǥ�� �ν����̶�� ����� ���ھ� +2, ������ ���ھ� -4�� ���ش�.
				score1 += 2;
				score2 -= 4;
				break aa;
			}

			if (killedMal == 12 && !((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// �������� �ε����� 12(�����Ź�)�̰� x,y�� ��ǥ�� �ν����� �ƴ϶�� ����� ���ھ� +2�� ���ش�.
				score1 += 2;
				break aa;
			}

			if (killedMal == 13 && ((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// �������� �ε����� 13(�����ֹ���)�̰� x,y�� ��ǥ�� �ν����̶�� ����� ���ھ� +4, ������ ���ھ� -8�� ���ش�.
				score1 += 4;
				score2 -= 8;
				break aa;
			}

			if (killedMal == 13 && !((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// �������� �ε����� 13(�����ֹ���)�̰� x,y�� ��ǥ�� �ν����� �ƴ϶�� ����� ���ھ� +4�� ���ش�.		
				score1 += 4;
				break aa;
			}

			if (killedMal == 14 && ((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// �������� �ε����� 14(��������)�̰� x,y�� ��ǥ�� �ν����̶�� ����� ���ھ� +1, ������ ���ھ� -2�� ���ش�.
				score1 += 1;
				score2 -= 2;
				break aa;
			}

			if (killedMal == 14 && !((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// �������� �ε����� 13(��������)�̰� x,y�� ��ǥ�� �ν����� �ƴ϶�� ����� ���ھ� +1�� ���ش�.
				score1 += 1;
				break aa;
			}
		}

		if (KoreaChess.myTurn == 0) { // ������϶� 
			scbar1 = new JLabel(score1.toString()); 
			scbar1.setFont(new Font("�������", Font.BOLD, 60));
			PlayerPanel[0].removeAll(); //����� �г��� ������ �����
			PlayerPanel[0].add(scbar1);// ������� ���� ������ ���� ��� ������ ���ڷ� �־��ش�.
			scbar2 = new JLabel(" " +score2.toString()+" ");  
			scbar2.setFont(new Font("�������", Font.BOLD, 60));
			PlayerPanel[1].removeAll();//������ �г��� ������ �����
			PlayerPanel[1].add(scbar2);//�������� ��� ������ ���� ��� ������ ���ڷ� �־��ش�.
		} else {
			scbar1 = new JLabel(score1.toString());
			scbar1.setFont(new Font("�������", Font.BOLD, 60));
			PlayerPanel[0].removeAll();
			PlayerPanel[0].add(scbar1);
			scbar2 = new JLabel(" " + score2.toString()+ " ");
			scbar2.setFont(new Font("�������", Font.BOLD, 60));
			PlayerPanel[1].removeAll();
			PlayerPanel[1].add(scbar2);
		}
		if (score1 >= 12) {
			endplay();
			JOptionPane.showMessageDialog(null,"����� �¸�!", "������ ����˴ϴ�.",JOptionPane.PLAIN_MESSAGE);
			System.exit(0);
		} else if (score2 >= 12) {
			endplay();
			JOptionPane.showMessageDialog(null,"������ �¸�!", "������ ����˴ϴ�.",JOptionPane.PLAIN_MESSAGE);
			System.exit(0);
		}
	}

	void DisplayMove(int Mal) { //���� Ŭ������ �� �гο� ���� �������� �̸� �����ִ� �Լ�
		String Icon = "";
		switch (Mal) {
		case 0:
			break;
		case 3:
			Icon = "images/movepo.jpg"; 
			//���콺�� Ŭ���Ǿ����� ���� �ε����� �������� �� ���� 3, �Ķ��� ǳ������ �������� �����ִ� �̹���
			break;
		case 5:
			Icon = "images/movesang.jpg";
			//���콺�� Ŭ���Ǿ����� ���� �ε����� �������� �� ���� 5, �Ķ��� �Ź��� �������� �����ִ� �̹���
			break;
		case 6:
			Icon = "images/movesa.jpg";
			//���콺�� Ŭ���Ǿ����� ���� �ε����� �������� �� ���� 6, �Ķ��� �ֹ����� �������� �����ִ� �̹���
			break;
		case 7:
			Icon = "images/movejol.jpg";
			//���콺�� Ŭ���Ǿ����� ���� �ε����� �������� �� ���� 7, �Ķ��� ������ �������� �����ִ� �̹���
			break;
		case 10:
			Icon = "images/moverpo.jpg";
			//���콺�� Ŭ���Ǿ����� ���� �ε����� �������� �� ���� 10, ������ ǳ������ �������� �����ִ� �̹���
			break;
		case 12:
			Icon = "images/moversang.jpg";
			//���콺�� Ŭ���Ǿ����� ���� �ε����� �������� �� ���� 12, ������ �Ź��� �������� �����ִ� �̹���
			break;
		case 13:
			Icon = "images/moversa.jpg";
			//���콺�� Ŭ���Ǿ����� ���� �ε����� �������� �� ���� 13, ������ �ֹ����� �������� �����ִ� �̹���
			break;
		case 14:
			Icon = "images/moverjol.jpg";
			//���콺�� Ŭ���Ǿ����� ���� �ε����� �������� �� ���� 14, ������ ������ �������� �����ִ� �̹���
			break;

		}
		if (Icon != "") { // �����ܰ�ü�� NULL�� �ƴ� ��� �����ܰ� �� �̹����� ��
			if ((Icon == "images/movepo.jpg") || (Icon == "images/movesa.jpg") || (Icon == "images/movesang.jpg")
					|| (Icon == "images/movejol.jpg") || (Icon == "images/moverpo.jpg")
					|| (Icon == "images/moversa.jpg") || (Icon == "images/moversang.jpg")
					|| (Icon == "images/moverjol.jpg"))
				display.removeAll(); // ���� �ǳڿ� ����ִ� ��� �̹����� �����Ѵ�
			display.add(new JLabel(new ImageIcon(Icon))); // �ǳڿ� �̹����� �־��ش�
		}
	}

	public Information() {
		setLayout(null);
		icon = new ImageIcon("Images/board.jpg");
		jp2 = new JPanel();
		jp2.setLayout(null);
		add(jp2);
		TitledBorder TB = new TitledBorder(new LineBorder(Color.black));
		Font font = new Font("Arial", Font.ITALIC, 20);
		RemainTime = new JLabel();
		RemainTime.setBounds(0, 0, 200, 100);
		RemainTime.setHorizontalAlignment(SwingConstants.CENTER);
		RemainTime.setText("00:00:00");
		RemainTime.setBorder(TB);
		RemainTime.setFont(font);

		HansuBack = new JButton();
		HansuBack.setBounds(0, 260, 100, 120);
		HansuBack.setVisible(false);
		HansuBack.setText("�Ѽ�������");
		HansuBack.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				KoreaChess.changeTurn(); // ü���������� ���� �ѱ�� ����.
				setTurnIsChangeToTrue();
			}
		});

		Player = new JToggleButton[2];
		for (int i = 0; i < 2; i++) {
			Player[i] = new JToggleButton();
			Player[i].setText("Player " + (i + 1));
			Player[i].setBorder(TB);
			Player[i].setBounds(100 * i, 130, 100, 30);
			Player[i].setEnabled(false);
			add(Player[i]);
		}
		Player[0].setSelected(true);

		PlayerPanel = new JPanel[2];
		for (int i = 0; i < 2; i++) {
			PlayerPanel[i] = new JPanel();
			PlayerPanel[i].setLayout(new FlowLayout());
			PlayerPanel[i].setBounds(100 * i, 160, 100, 100);
			PlayerPanel[i].setBorder(TB);
			add(PlayerPanel[i]);
		}

		Startbu = new JButton();
		Startbu.setBounds(0, 260, 100, 120);
		Startbu.setText("����");
		Startbu.addMouseListener(new ButtonMouseListener());
		Endbu = new JButton();
		Endbu.setBounds(100, 260, 100, 120);
		Endbu.setText("������");
		Endbu.addMouseListener(new ButtonMouseListener());

		turnColor.setBounds(0, 400, 200, 120);
		turnColor.setBackground(Color.BLUE);

		display = new JPanel();
		display.setBounds(0, 550, 200, 240);

		add(RemainTime);
		add(HansuBack);
		add(Startbu);
		add(Endbu);
		add(turnColor);
		add(display);

		setFocusable(false);
		setLocation(785, 0);
		setSize(200, 800);
		setVisible(true);
		PlayTimer = new PlayTimer();
		RemainTimer = new RemainTimer();

	}

	class PlayTimer extends Thread {
		void timer1() {// �÷��� �ð�
			xx = (System.currentTimeMillis() - oo) / 1000d;
			hours = ((int) xx % 86400) / 3600;
			mins = ((int) xx % 3600) / 60;
			secs = (int) xx % 60;
			PlayTime.setText(String.format("%02d:%02d:%02d  ", hours, mins, secs));
			// le.repaint();
		}

		public void run() {
			// while (true) {
			while (true) {
				try {
					if (loop) {
						Thread.sleep(100);
						timer1();
					} else {
						Thread.sleep(1000 * 60 * 60 * 24); // 24�ð� ��������
					}
				} catch (InterruptedException e) {
					break;
				}
			}
			// }
		}
	}

	class RemainTimer extends Thread {
		void timer() {// �����ð�
			xx1 = (oo1 + (60000d) - System.currentTimeMillis()) / 1000d;
			hours1 = ((int) xx1 % 86400) / 3600;
			mins1 = ((int) xx1 % 3600) / 60;
			secs1 = (int) xx1 % 60;
			if (secs1 >= 0)
				RemainTime.setText(String.format("%02d:%02d:%02d  ", hours1, mins1, secs1));
			// ���� �ٲ���ų� �ð��� �ʰ�������
			if (secs1 <= 0 || TurnIsChange) {
				if (secs1 <= 0) {// ���� ���°�
									// �ð��ʰ����
					KoreaChess.changeTurn();
					setTurnIsChangeToTrue();
				} // ���� �ٲ۴�
				oo1 = System.currentTimeMillis();
				TurnIsChange = false;
			}
		}

		public void run() {
			// while (true) {
			while (true) {
				try {
					if (loop) {
						Thread.sleep(100);
						timer();
					} else {
						Thread.sleep(1000 * 60 * 60 * 24); // 24�ð� ��������
					}
				} catch (InterruptedException e) {
					break;
				}
				// }
			}
		}

	}

	class ButtonMouseListener implements MouseListener {

		@SuppressWarnings("deprecation")
		@Override
		public void mouseClicked(MouseEvent e) {
			if (e.getSource() == Startbu) {
				startplay();

				if (first) {// ó�� ���� ��������(ó�� �����Ҷ�)
					loop = true;
					oo = System.currentTimeMillis();// ���� �ð��� ���Ѵ�.
					oo1 = System.currentTimeMillis();// ���� �ð��� ����
					RemainTimer.start();
					first = false;
				} else {// ������ ������ ���� ��������(ó�� ������ �ƴҶ�)
					oo = System.currentTimeMillis();
					oo1 = System.currentTimeMillis();
					RemainTimer.resume();
				}
				IsStart = true;
				HansuBack.setVisible(true);
				Startbu.setVisible(false);
			} else if (e.getSource() == Endbu) { // ������ ��ư�� ������ ���Ḧ ����� Ȯ�� �� ���� ��ҽ� ��� ����
				int i =JOptionPane.showConfirmDialog(null,"���� �����Ͻðڽ��ϱ�?", "����",JOptionPane.OK_CANCEL_OPTION,JOptionPane.INFORMATION_MESSAGE);
				if(i == 0){
				System.out.println("��");
				System.exit(0);
				}
				else
				System.out.println("�ƴϿ�");
			}
		}

		@Override
		public void mouseEntered(MouseEvent e) {
		}

		@Override
		public void mouseExited(MouseEvent e) {
		}

		@Override
		public void mousePressed(MouseEvent e) {
		}

		@Override
		public void mouseReleased(MouseEvent e) {
		}

	}
}
