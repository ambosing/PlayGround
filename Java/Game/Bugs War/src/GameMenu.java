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
		
		JMenu fileMenu = new JMenu("�޴�");
		JMenuItem New = new JMenuItem("�� ����");
		JMenuItem Save = new JMenuItem("�Ͻ�����");
		JMenuItem Exit = new JMenuItem("�ݱ�"); // ���� �׼Ǹ����� �߰�.

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

		JMenu editMenu = new JMenu("����");
		JMenuItem Edit = new JMenuItem("����");
		JMenuItem Creater = new JMenuItem("���� ��");

		editMenu.add(Edit);
		editMenu.addSeparator();
		editMenu.add(Creater);

		add(fileMenu);
		add(editMenu);

		Creater.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				JOptionPane.showMessageDialog(null, "������, ������, �ֱǴ�", "���� ��", 1); // ���߿����������ξ������ؼ����ʿ�
			}
		});

		setVisible(true);
	}
}
