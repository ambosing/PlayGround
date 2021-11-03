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

	void setTurnIsChangeToTrue() {// TurnIsChange를 True로 만듬.턴이바뀌면 남은시간 초기화를 위해서
		TurnIsChange = true;
		SetTurn();
	}

	void SetTurn() {// 턴이 바뀌면 토글버튼도 바뀌게
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
	      File soundFile = new File("Music/LDie.wav");  // File 값 받기
	      AudioInputStream audioInputStream = AudioSystem.getAudioInputStream(soundFile);
	      // 받아온 File 지정된 오디오 입력 스트림을 변환해, 나타난 인코딩의 오디오 입력 스트림을 취득 
	      
	      AudioFormat audioFormat = audioInputStream.getFormat();
	      // 바이트수는 아니고 샘플 프레임수로 나타내지는, 스트림의 길이를 취득

	      DataLine.Info info = new DataLine.Info(SourceDataLine.class,audioFormat);
	      // 단일의 오디오 형식을 포함한 지정한 정보로부터 데이터 라인의 정보 오브젝트를 구축

	      SourceDataLine line = (SourceDataLine) AudioSystem.getLine(info);
	      // 지정된 Line.Info 오브젝트의 기술에 일치하는 라인을 취득

	      line.open(audioFormat);
	     // 지정된 형식과 지정된 버퍼 사이즈로 라인을 열어, 라인이 필요한 system resource를 획득해 조작 가능
	      line.start();
	    // 라인에서의 데이터 입출력을 가능

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
	      File startFile = new File("Music/1-Up.wav");  // File 값 받기
	      AudioInputStream startInputStream = AudioSystem.getAudioInputStream(startFile);
	      // 받아온 File 지정된 오디오 입력 스트림을 변환해, 나타난 인코딩의 오디오 입력 스트림을 취득 
	      
	      AudioFormat startFormat = startInputStream.getFormat();
	      // 바이트수는 아니고 샘플 프레임수로 나타내지는, 스트림의 길이를 취득

	      DataLine.Info startinfo = new DataLine.Info(SourceDataLine.class,startFormat);
	      // 단일의 오디오 형식을 포함한 지정한 정보로부터 데이터 라인의 정보 오브젝트를 구축

	      SourceDataLine startline = (SourceDataLine) AudioSystem.getLine(startinfo);
	      // 지정된 Line.Info 오브젝트의 기술에 일치하는 라인을 취득

	      startline.open(startFormat);
	     // 지정된 형식과 지정된 버퍼 사이즈로 라인을 열어, 라인이 필요한 system resource를 획득해 조작 가능
	      startline.start();
	    // 라인에서의 데이터 입출력을 가능

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
	     // File 값 받기
	      File ending = new File("Music/ending.wav");
	      // 받아온 File 지정된 오디오 입력 스트림을 변환해, 나타난 인코딩의 오디오 입력 스트림을 취득 
	      AudioInputStream endInputStream = AudioSystem.getAudioInputStream(ending);
	      
	      AudioFormat endFormat = endInputStream.getFormat();
	      // 바이트수는 아니고 샘플 프레임수로 나타내지는, 스트림의 길이를 취득

	      // 단일의 오디오 형식을 포함한 지정한 정보로부터 데이터 라인의 정보 오브젝트를 구축
	      DataLine.Info endinfo = new DataLine.Info(SourceDataLine.class,endFormat);

	      SourceDataLine endline = (SourceDataLine) AudioSystem.getLine(endinfo);
	      // 지정된 Line.Info 오브젝트의 기술에 일치하는 라인을 취득

	     // 지정된 형식과 지정된 버퍼 사이즈로 라인을 열어, 라인이 필요한 system resource를 획득해 조작 가능
	      endline.open(endFormat);
	    // 라인에서의 데이터 입출력을 가능
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
		// 말의 인덱스와, 말이 죽은 인덱스의 x좌표와, y좌표를 매개변수로 받아 실행하는 함수
		play(); //말이 잡혔을때 잡아 먹히는 소리 실행
		aa: { // 말이 캔디존에서 잡힐때와 그렇지 않은곳에서 잡힐때 각 점수 계산하는 함수.
			if ((killedMal == 3) && ((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// 잡힌말의 인덱스가 3(파란풍뎅이)이고 x,y의 좌표가 부시존이라면 빨간팀 스코어 +3, 블루팀 스코어 -6을 해준다.
				score2 += 3;
				score1 -= 6;
				break aa;
			}

			if (killedMal == 3 && !((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// 잡힌말의 인덱스가 3(파란풍뎅이)이고 x,y의 좌표가 부시존이 아니라면 빨간팀 스코어 +3을 해준다.
				score2 += 3;
				break aa;
			}

			if (killedMal == 5 && ((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// 잡힌말의 인덱스가 5(파란거미)이고 x,y의 좌표가 부시존이라면 빨간팀 스코어 +2, 블루팀 스코어 -4을 해준다.
				score2 += 2;
				score1 -= 4;
				break aa;
			}

			if (killedMal == 5 && !((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// 잡힌말의 인덱스가 5(파란거미)이고 x,y의 좌표가 부시존이 아니라면 빨간팀 스코어 +2을 해준다.
				score2 += 2;
				break aa;
			}

			if (killedMal == 6 && ((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// 잡힌말의 인덱스가 6(파란애벌레)이고 x,y의 좌표가 부시존이라면 빨간팀 스코어 +4, 블루팀 스코어 -8을 해준다.
				score2 += 4;
				score1 -= 8;
				break aa;
			}

			if (killedMal == 6 && !((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// 잡힌말의 인덱스가 6(파란애벌레)이고 x,y의 좌표가 부시존이 아니라면 빨간팀 스코어 +4을 해준다.
				score2 += 4;
				break aa;

			}

			if (killedMal == 7 && ((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// 잡힌말의 인덱스가 7(파란개미)이고 x,y의 좌표가 부시존이라면 빨간팀 스코어 +1, 블루팀 스코어 -2을 해준다.
				score2 += 1;
				score1 -= 2;
				break aa;
			}

			if (killedMal == 7 && !((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// 잡힌말의 인덱스가 7(파란개미)이고 x,y의 좌표가 부시존이 아니라면 빨간팀 스코어 +1을 해준다.
				score2 += 1;
				break aa;
			}

			if (killedMal == 10 && ((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// 잡힌말의 인덱스가 10(빨간풍뎅이)이고 x,y의 좌표가 부시존이라면 블루팀 스코어 +3, 빨간팀 스코어 -6을 해준다.
				score1 += 3;
				score2 -= 6;
				break aa;
			}

			if (killedMal == 10 && !((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// 잡힌말의 인덱스가 10(빨간풍뎅이)이고 x,y의 좌표가 부시존이 아니라면 블루팀 스코어 +3을 해준다.
				score1 += 3;
				break aa;
			}

			if (killedMal == 12 && ((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// 잡힌말의 인덱스가 12(빨간거미)이고 x,y의 좌표가 부시존이라면 블루팀 스코어 +2, 빨간팀 스코어 -4을 해준다.
				score1 += 2;
				score2 -= 4;
				break aa;
			}

			if (killedMal == 12 && !((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// 잡힌말의 인덱스가 12(빨간거미)이고 x,y의 좌표가 부시존이 아니라면 블루팀 스코어 +2을 해준다.
				score1 += 2;
				break aa;
			}

			if (killedMal == 13 && ((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// 잡힌말의 인덱스가 13(빨간애벌레)이고 x,y의 좌표가 부시존이라면 블루팀 스코어 +4, 빨간팀 스코어 -8을 해준다.
				score1 += 4;
				score2 -= 8;
				break aa;
			}

			if (killedMal == 13 && !((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// 잡힌말의 인덱스가 13(빨간애벌레)이고 x,y의 좌표가 부시존이 아니라면 블루팀 스코어 +4을 해준다.		
				score1 += 4;
				break aa;
			}

			if (killedMal == 14 && ((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// 잡힌말의 인덱스가 14(빨간개미)이고 x,y의 좌표가 부시존이라면 블루팀 스코어 +1, 빨간팀 스코어 -2을 해준다.
				score1 += 1;
				score2 -= 2;
				break aa;
			}

			if (killedMal == 14 && !((x == 5 || x == 6) && (y == 7 || y == 8))) {
			// 잡힌말의 인덱스가 13(빨간개미)이고 x,y의 좌표가 부시존이 아니라면 블루팀 스코어 +1을 해준다.
				score1 += 1;
				break aa;
			}
		}

		if (KoreaChess.myTurn == 0) { // 블루팀일때 
			scbar1 = new JLabel(score1.toString()); 
			scbar1.setFont(new Font("맑은고딕", Font.BOLD, 60));
			PlayerPanel[0].removeAll(); //블루팀 패널의 내용을 지운다
			PlayerPanel[0].add(scbar1);// 블루팀이 얻은 점수를 맑은 고딕 형식의 문자로 넣어준다.
			scbar2 = new JLabel(" " +score2.toString()+" ");  
			scbar2.setFont(new Font("맑은고딕", Font.BOLD, 60));
			PlayerPanel[1].removeAll();//레드팀 패널의 내용을 지운다
			PlayerPanel[1].add(scbar2);//레드팀이 어든 점수를 맑은 고딕 형시의 문자로 넣어준다.
		} else {
			scbar1 = new JLabel(score1.toString());
			scbar1.setFont(new Font("맑은고딕", Font.BOLD, 60));
			PlayerPanel[0].removeAll();
			PlayerPanel[0].add(scbar1);
			scbar2 = new JLabel(" " + score2.toString()+ " ");
			scbar2.setFont(new Font("맑은고딕", Font.BOLD, 60));
			PlayerPanel[1].removeAll();
			PlayerPanel[1].add(scbar2);
		}
		if (score1 >= 12) {
			endplay();
			JOptionPane.showMessageDialog(null,"블루팀 승리!", "게임이 종료됩니다.",JOptionPane.PLAIN_MESSAGE);
			System.exit(0);
		} else if (score2 >= 12) {
			endplay();
			JOptionPane.showMessageDialog(null,"레드팀 승리!", "게임이 종료됩니다.",JOptionPane.PLAIN_MESSAGE);
			System.exit(0);
		}
	}

	void DisplayMove(int Mal) { //말을 클릭했을 때 패널에 말의 움직임을 미리 보여주는 함수
		String Icon = "";
		switch (Mal) {
		case 0:
			break;
		case 3:
			Icon = "images/movepo.jpg"; 
			//마우스가 클릭되었을때 말의 인덱스를 가져오고 그 값이 3, 파란색 풍뎅이의 움직임을 보여주는 이미지
			break;
		case 5:
			Icon = "images/movesang.jpg";
			//마우스가 클릭되었을때 말의 인덱스를 가져오고 그 값이 5, 파란색 거미의 움직임을 보여주는 이미지
			break;
		case 6:
			Icon = "images/movesa.jpg";
			//마우스가 클릭되었을때 말의 인덱스를 가져오고 그 값이 6, 파란색 애벌레의 움직임을 보여주는 이미지
			break;
		case 7:
			Icon = "images/movejol.jpg";
			//마우스가 클릭되었을때 말의 인덱스를 가져오고 그 값이 7, 파란색 개미의 움직임을 보여주는 이미지
			break;
		case 10:
			Icon = "images/moverpo.jpg";
			//마우스가 클릭되었을때 말의 인덱스를 가져오고 그 값이 10, 빨간색 풍뎅이의 움직임을 보여주는 이미지
			break;
		case 12:
			Icon = "images/moversang.jpg";
			//마우스가 클릭되었을때 말의 인덱스를 가져오고 그 값이 12, 빨간색 거미의 움직임을 보여주는 이미지
			break;
		case 13:
			Icon = "images/moversa.jpg";
			//마우스가 클릭되었을때 말의 인덱스를 가져오고 그 값이 13, 빨간색 애벌레의 움직임을 보여주는 이미지
			break;
		case 14:
			Icon = "images/moverjol.jpg";
			//마우스가 클릭되었을때 말의 인덱스를 가져오고 그 값이 14, 빨간색 개미의 움직임을 보여주는 이미지
			break;

		}
		if (Icon != "") { // 아이콘객체가 NULL이 아닐 경우 아이콘과 각 이미지를 비교
			if ((Icon == "images/movepo.jpg") || (Icon == "images/movesa.jpg") || (Icon == "images/movesang.jpg")
					|| (Icon == "images/movejol.jpg") || (Icon == "images/moverpo.jpg")
					|| (Icon == "images/moversa.jpg") || (Icon == "images/moversang.jpg")
					|| (Icon == "images/moverjol.jpg"))
				display.removeAll(); // 현재 판넬에 들어있는 모든 이미지를 삭제한다
			display.add(new JLabel(new ImageIcon(Icon))); // 판넬에 이미지를 넣어준다
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
		HansuBack.setText("한수물리기");
		HansuBack.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				KoreaChess.changeTurn(); // 체인지턴으로 턴을 넘길수 있음.
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
		Startbu.setText("시작");
		Startbu.addMouseListener(new ButtonMouseListener());
		Endbu = new JButton();
		Endbu.setBounds(100, 260, 100, 120);
		Endbu.setText("끝내기");
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
		void timer1() {// 플레이 시간
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
						Thread.sleep(1000 * 60 * 60 * 24); // 24시간 정지상태
					}
				} catch (InterruptedException e) {
					break;
				}
			}
			// }
		}
	}

	class RemainTimer extends Thread {
		void timer() {// 남은시간
			xx1 = (oo1 + (60000d) - System.currentTimeMillis()) / 1000d;
			hours1 = ((int) xx1 % 86400) / 3600;
			mins1 = ((int) xx1 % 3600) / 60;
			secs1 = (int) xx1 % 60;
			if (secs1 >= 0)
				RemainTime.setText(String.format("%02d:%02d:%02d  ", hours1, mins1, secs1));
			// 턴이 바뀌었거나 시간이 초과됐을때
			if (secs1 <= 0 || TurnIsChange) {
				if (secs1 <= 0) {// 만약 상태가
									// 시간초과라면
					KoreaChess.changeTurn();
					setTurnIsChangeToTrue();
				} // 턴을 바꾼다
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
						Thread.sleep(1000 * 60 * 60 * 24); // 24시간 정지상태
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

				if (first) {// 처음 시작 눌렀을때(처음 실행할때)
					loop = true;
					oo = System.currentTimeMillis();// 기준 시간을 정한다.
					oo1 = System.currentTimeMillis();// 기준 시간을 정함
					RemainTimer.start();
					first = false;
				} else {// 끝내기 누른후 시작 눌렀을때(처음 실행이 아닐때)
					oo = System.currentTimeMillis();
					oo1 = System.currentTimeMillis();
					RemainTimer.resume();
				}
				IsStart = true;
				HansuBack.setVisible(true);
				Startbu.setVisible(false);
			} else if (e.getSource() == Endbu) { // 끝내기 버튼을 누르면 종료를 물어보며 확인 시 종료 취소시 계속 진행
				int i =JOptionPane.showConfirmDialog(null,"정말 종료하시겠습니까?", "종료",JOptionPane.OK_CANCEL_OPTION,JOptionPane.INFORMATION_MESSAGE);
				if(i == 0){
				System.out.println("예");
				System.exit(0);
				}
				else
				System.out.println("아니요");
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
