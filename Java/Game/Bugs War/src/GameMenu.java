import java.awt.*;
import java.awt.event.*;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;


@SuppressWarnings("serial")
public class GameMenu extends JMenuBar  {
	JFrame closeFrame = new JFrame();
	GameMenu() {
		
		JMenu fileMenu = new JMenu("메뉴");
		JMenuItem New = new JMenuItem("새 게임");
		JMenuItem Save = new JMenuItem("일시정지");
		JMenuItem Exit = new JMenuItem("닫기"); // 종료 액션리스너 추가.

		New.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0 ){
				Information.score1 =0;
				Information.score2=0;
				KoreaChess newone = new KoreaChess();
				closeFrame.dispose();
				setVisible(false);
			}
		});
		
		Save.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0){
			
			}
		});
		

		Exit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				System.exit(0);
			}
		});
		

		fileMenu.add(New);
		fileMenu.addSeparator();
		fileMenu.add(Save);
		fileMenu.addSeparator();
		fileMenu.add(Exit);

		JMenu editMenu = new JMenu("편집");
		JMenuItem Edit = new JMenuItem("편집");
		JMenuItem Creater = new JMenuItem("만든 이");

		editMenu.add(Edit);
		editMenu.addSeparator();
		editMenu.add(Creater);

		add(fileMenu);
		add(editMenu);

		Creater.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				JOptionPane.showMessageDialog(null, "최정윤, 양지원, 주권능", "만든 이", 1); // 나중에세부적으로쓰기위해수정필요
			}
		});

		setVisible(true);
	}
}
