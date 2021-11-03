import java.awt.*;
import java.io.File;

import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.DataLine;
import javax.sound.sampled.SourceDataLine;
import javax.swing.*;



public class CheckMove extends Information {
	
	
	public boolean CheackMalMove(int[][] board, int i, int[] preposition, int[] nowposition)
	/*������� ��ǥ��, ���� ���� ��ǥ, ���� �̵��� ������ǥ�� �޾� boolean type�� ��ȯ. true�� ������, false�� �������� ����.*/
	{
		
		if (i == 6 || i == 13) { // �ֹ��� ������ ����. 
			if (checkOneWorm(board, preposition, nowposition)) {
				return true;
			} else
				return false;
		} else if (i % 7 == 3) { // ǳ���� ������ ����. countSomeBeetle�� 0�̵Ǹ� �����Ѵ�.
			if (countSomeBeetle(board, preposition, nowposition) == 0) {
				candyZoneScore3(board,preposition,nowposition);
				return true;
			} else
				return false;
		}

		else if (i % 7 == 5) { // �Ź� ������ ���� countsomeSpider�� 0�� �Ǹ� �����Ѵ�.
			if (countSomeSpider(board, preposition, nowposition) == 0) {
				candyZoneScore2(board,preposition,nowposition);
				return true;
			} else
				return false;
		} 
		
		else if (i == 7) { // �Ķ� ���� ������ ����. �Ķ� ���̴� y��ǥ�� �������� -���� �� �� ����.
			if (checkOneAnt(board, preposition, nowposition) == 0) {
				if ((preposition[1] - nowposition[1]) <= 0) {
					candyZoneScore1(board,preposition,nowposition);
					return true;
				}
			}
			return false;
		} 
		
		else if (i == 14) { // �������� ������ ���� �ڷ� ������. ���� ���̴� y��ǥ�� �������� +���� �� �� ����.
			if (checkOneAnt(board, preposition, nowposition) == 0) {
				if ((preposition[1] - nowposition[1]) >= 0) {
					candyZoneScore1(board,preposition,nowposition);
					return true;
				}
			}
			return false;
		}

		return true; //�Լ��� ȣ���� �ݷ����� ���ϰ� true�� �����ش�.
	}
	
	/*������ �������� �����ϴ� �Լ�. ������� �ε����� ���� ���̰� �ִ� ��ġ, ���̰� ������ ���� ��ǥ�� �޴´�.
	 ���̰� ������ x��ǥ�� ���̿� y��ǥ�� ���̸� ������ ������ ���� ������ ���̵Ǹ� ���̰� ������ ��ǥ�� ��ȯ���ش�.*/
	public int checkOneAnt(int[][] board, int[] preposition, int[] nowposition) {
		int a, b;

		a = preposition[0] - nowposition[0];
		b = preposition[1] - nowposition[1];
		
		/*�ν��������� �̵��� ���� ���ǹ�. �ν����� ��ǥ�� �̵��ϰ� �� ��� ��� �޼����� �Բ� ���ϰ�1�� ��ȯ. �� �������� ���Ѵ�.*/
		if(((nowposition[0] == 2 || nowposition[0] == 9) && (nowposition[1] == 5 || nowposition[1] == 10)) 
			|| (nowposition[0] == 5 && nowposition[1] == 2) ||(nowposition[0] == 6 && nowposition [1] == 13)){
			JOptionPane.showConfirmDialog(null, "�ν������� �̵��Ͻ� �� �����ϴ�.", "---------------------���------------------",
					JOptionPane.WARNING_MESSAGE);
			return 1;
		}
		
		if ((a * a + b * b) == 1)
			return 0;
		else if (((a * a + b * b) == 4) && (nowposition[1] - preposition[1] == 2))
			return board[preposition[0]][preposition[1] + 1];
		
		else if (((a * a + b * b) == 4) && (nowposition[1] - preposition[1] == -2))
			
			return board[preposition[0]][preposition[1] - 1];
		else if (((a * a + b * b) == 4) && (nowposition[0] - preposition[0] == 2))
			
			return board[preposition[0] + 1][preposition[1]];
		else if (((a * a + b * b) == 4) && (nowposition[0] - preposition[0] == -2))
			
			return board[preposition[0] - 1][preposition[1]];
		else
			return 1;
	}
	
	/*�ֹ����� �������� �����ϴ� �Լ�. ������� �ε����� ���� �ֹ����� �ִ� ��ġ, �ֹ����� ������ ���� ��ǥ�� �޴´�.
	 �ֹ����� ������ x��ǥ�� ���̿� y��ǥ�� ���̸� ������ ������ ���� ������ ���̵Ǹ� �ֹ����� ������ ��ǥ�� ��ȯ���ش�.*/
	public boolean checkOneWorm(int board[][], int[] preposition, int[] nowposition) {

		int a, b;

		a = preposition[0] - nowposition[0];
		b = preposition[1] - nowposition[1];
		
		if(((nowposition[0] == 2 || nowposition[0] == 9) && (nowposition[1] == 5 || nowposition[1] == 10)) 
				|| (nowposition[0] == 5 && nowposition[1] == 2) ||(nowposition[0] == 6 && nowposition [1] == 13)){
				JOptionPane.showConfirmDialog(null, "�ν������� �̵��Ͻ� �� �����ϴ�.", "---------------------���------------------",
						JOptionPane.WARNING_MESSAGE);
				return false;
			}
		
		
		if ((a * a + b * b) == 1){
			candyZoneScore4(board, preposition, nowposition);
			return true;
			}
		else if (countSomeWorm(board, preposition, nowposition) == 0){
			candyZoneScore4(board, preposition, nowposition);
			return true;
			}
			
		else
			return false;
		
	}
	
	/*�ֹ����� �밢�� �������� �����ϴ� �Լ�. ������� �ε����� ���� �ֹ����� �ִ� ��ġ, �ֹ����� ������ ���� ��ǥ�� �޴´�.
	 �ֹ����� ������ x��ǥ�� ���̿� y��ǥ�� ���̸� ������ ������ ���� ������ ���̵Ǹ� �ֹ����� ������ ��ǥ�� ��ȯ���ش�.*/
	public int countSomeWorm(int[][] board, int[] preposition, int[] nowposition) {
																																						
		if (nowposition[0] - preposition[0] == 1 && nowposition[1] - preposition[1] == 1) {
			return 0;
		} else if (nowposition[0] - preposition[0] == 1 && nowposition[1] - preposition[1] == -1) {
			return 0;
		} else if (nowposition[0] - preposition[0] == -1 && nowposition[1] - preposition[1] == 1) {
			return 0;
		} else if (nowposition[0] - preposition[0] == -1 && nowposition[1] - preposition[1] == -1) {
			return 0;
		}

		else
			return 1;
	}

	/*ǳ������ �������� �����ϴ� �Լ�. ������� �ε����� ���� ǳ���̰� �ִ� ��ġ, ǳ���̰� ������ ���� ��ǥ�� �޴´�.
	 �ֹ����� ������ x��ǥ�� ���̿� y��ǥ�� ���̸� ������ ������ ���� ������ ���̵Ǹ� �ֹ����� ������ ��ǥ�� ��ȯ���ش�.
	 */
	public int countSomeBeetle(int[][] board, int[] preposition, int[] nowposition) {
		/*ǳ������ x��ǥ�� 0�̿������� ������ ����. ǳ���̰� ���� �ִ� x,y ��ǥ ������ ������ �����¿� �ε����� 0�� �ƴϸ�(������� ������) 
		 * ������ �� ����. ǳ���̴� �����¿� ��ĭ �տ� �ε��� ���� ������ �� ���� �ִ� 2�� ���̸� ���� ��ǥ�� ������ �� �ִ�.*/
		if (preposition[1] == 0) {
			if (board[preposition[0]][preposition[1] + 1] != 0) {
				if ((preposition[0] == nowposition[0]) && (preposition[1] + 2 == nowposition[1]))
					return 0;
				else if ((preposition[0] == nowposition[0]) && (preposition[1] + 3 == nowposition[1]))
					return 0;
				else
					return 1;
			} else if (board[preposition[0] + 1][preposition[1]] != 0) {
				if ((preposition[0] + 2 == nowposition[0]) && (preposition[1] == nowposition[1]))
					return 0;
				else if ((preposition[0] + 3 == nowposition[0]) && (preposition[1] == nowposition[1]))
					return 0;
				else
					return 1;
			} else if (board[preposition[0] - 1][preposition[1]] != 0) {
				if ((preposition[0] - 2 == nowposition[0]) && (preposition[1] == nowposition[1]))
					return 0;
				else if ((preposition[0] - 3 == nowposition[0]) && (preposition[1] == nowposition[1]))
					return 0;
				else
					return 1;
			} else if (board[preposition[0] - 2][preposition[1]] != 0) {
				if ((preposition[0] - 3 == nowposition[0]) && (preposition[1] == nowposition[1]))
					return 0;
				else
					return 1;
			} else if (board[preposition[0] + 2][preposition[1]] != 0) {
				if ((preposition[0] + 3 == nowposition[0]) && (preposition[1] == nowposition[1]))
					return 0;
				else
					return 1;
			} else if (board[preposition[0]][preposition[1] + 2] != 0) {
				if ((preposition[0] == nowposition[0]) && (preposition[1] + 3 == nowposition[1]))
					return 0;
				else
					return 1;
			}
		} 
		else if (preposition[0] == 0) {
			if (board[preposition[0]][preposition[1] + 1] != 0) {
				if ((preposition[0] == nowposition[0]) && (preposition[1] + 2 == nowposition[1]))
					return 0;
				else if ((preposition[0] == nowposition[0]) && (preposition[1] + 3 == nowposition[1]))
					return 0;
				else
					return 1;
			}
			if (board[preposition[0]][preposition[1] - 1] != 0) {
				if ((preposition[0] == nowposition[0]) && (preposition[1] - 2 == nowposition[1]))
					return 0;
				else if ((preposition[0] == nowposition[0]) && (preposition[1] - 3 == nowposition[1]))
					return 0;
				else
					return 1;
			} else if (board[preposition[0] + 1][preposition[1]] != 0) {
				if ((preposition[0] + 2 == nowposition[0]) && (preposition[1] == nowposition[1]))
					return 0;
				else if ((preposition[0] + 3 == nowposition[0]) && (preposition[1] == nowposition[1]))
					return 0;
				else
					return 1;
			} else if (board[preposition[0] + 2][preposition[1]] != 0) {
				if ((preposition[0] + 3 == nowposition[0]) && (preposition[1] == nowposition[1]))
					return 0;
				else
					return 1;
			} else if (board[preposition[0]][preposition[1] - 2] != 0) {
				if ((preposition[0] == nowposition[0]) && (preposition[1] - 3 == nowposition[1]))
					return 0;
				else
					return 1;
			} else if (board[preposition[0]][preposition[1] + 2] != 0) {
				if ((preposition[0] == nowposition[0]) && (preposition[1] + 3 == nowposition[1]))
					return 0;
				else
					return 1;
			}
		}
		
		/*ǳ���̰� ���� �ִ� �ε����� y��ǥ�� 15���ٸ� y�� 15 �̻��� �����δ� �Ѿ �� ����.(������� ��ǥ�� �Ѿ��.)*/
		else if (preposition[1] == 15) {
				if (board[preposition[0]][preposition[1] - 1] != 0) {
					if ((preposition[0] == nowposition[0]) && (preposition[1] - 2 == nowposition[1]))
						return 0;
					else if ((preposition[0] == nowposition[0]) && (preposition[1] - 3 == nowposition[1]))
						return 0;
					else
						return 1;
				} else if (board[preposition[0] + 1][preposition[1]] != 0) {
					if ((preposition[0] + 2 == nowposition[0]) && (preposition[1] == nowposition[1]))
						return 0;
					else if ((preposition[0] + 3 == nowposition[0]) && (preposition[1] == nowposition[1]))
						return 0;
					else
						return 1;
				} else if (board[preposition[0] - 1][preposition[1]] != 0) {
					if ((preposition[0] - 2 == nowposition[0]) && (preposition[1] == nowposition[1]))
						return 0;
					else if ((preposition[0] - 3 == nowposition[0]) && (preposition[1] == nowposition[1]))
						return 0;
					else
						return 1;
				} else if (board[preposition[0] - 2][preposition[1]] != 0) {
					if ((preposition[0] - 3 == nowposition[0]) && (preposition[1] == nowposition[1]))
						return 0;
					else
						return 1;
				} else if (board[preposition[0]][preposition[1] - 2] != 0) {
					if ((preposition[0] == nowposition[0]) && (preposition[1] - 3 == nowposition[1]))
						return 0;
					else
						return 1;
				} else if (board[preposition[0]][preposition[1] + 2] != 0) {
					if ((preposition[0] == nowposition[0]) && (preposition[1] + 3 == nowposition[1]))
						return 0;
					else
						return 1;
				}
			} 
		
		/*ǳ���̰� ���� �ִ� �ε����� x��ǥ�� 11���ٸ� x�� 11 �̻��� �����δ� �Ѿ �� ����.(������� ��ǥ�� �Ѿ��.)*/
		else if (preposition[0] == 11) {
				if (board[preposition[0]][preposition[1] + 1] != 0) {
					if ((preposition[0] == nowposition[0]) && (preposition[1] + 2 == nowposition[1]))
						return 0;
					else if ((preposition[0] == nowposition[0]) && (preposition[1] + 3 == nowposition[1]))
						return 0;
					else
						return 1;
				}
				if (board[preposition[0]][preposition[1] - 1] != 0) {
					if ((preposition[0] == nowposition[0]) && (preposition[1] - 2 == nowposition[1]))
						return 0;
					else if ((preposition[0] == nowposition[0]) && (preposition[1] - 3 == nowposition[1]))
						return 0;
					else
						return 1;
				} else if (board[preposition[0] - 1][preposition[1]] != 0) {
					if ((preposition[0] - 2 == nowposition[0]) && (preposition[1] == nowposition[1]))
						return 0;
					else if ((preposition[0] - 3 == nowposition[0]) && (preposition[1] == nowposition[1]))
						return 0;
					else
						return 1;
				} else if (board[preposition[0] - 2][preposition[1]] != 0) {
					if ((preposition[0] - 3 == nowposition[0]) && (preposition[1] == nowposition[1]))
						return 0;
					else
						return 1;
				} else if (board[preposition[0]][preposition[1] - 2] != 0) {
					if ((preposition[0] == nowposition[0]) && (preposition[1] - 3 == nowposition[1]))
						return 0;
					else
						return 1;
				} else if (board[preposition[0]][preposition[1] + 2] != 0) {
					if ((preposition[0] == nowposition[0]) && (preposition[1] + 3 == nowposition[1]))
						return 0;
					else
						return 1;
				}
			}
		
		/*ǳ���̸� �������� �����¿��� �ε����� � ���� �ִٸ� ǳ���̴� ������ �� �ִ�. �� �پ� ���� �� �ִ�. ǳ���̰� ������ ��ǥ�� ǳ���̰� ������ ��
		 * �ִ� ������� 0���� ��ȯ���ش�. �Լ��� ȣ���� �ݷ����� 0���� �����ϰ� �Ǹ� ǳ���̴� ������ �� �ִ�.   */
		else{
			if ((board[preposition[0]][preposition[1] + 1] != 0)||(board[preposition[0]][preposition[1] - 1] != 0)
		               ||(board[preposition[0]-1][preposition[1]] != 0)||(board[preposition[0] + 1][preposition[1]] != 0)) 
			{
		            if ((preposition[0] == nowposition[0]) && (preposition[1] + 2 == nowposition[1]))
		               return 0;
		            else if ((preposition[0] == nowposition[0]) && (preposition[1] + 3 == nowposition[1]))
		               return 0;
		            else if ((preposition[0] == nowposition[0]) && (preposition[1] - 2 == nowposition[1]))
		               return 0;
		            else if ((preposition[0] == nowposition[0]) && (preposition[1] - 3 == nowposition[1]))
		               return 0;
		            else if ((preposition[0] - 2 == nowposition[0]) && (preposition[1] == nowposition[1]))
		               return 0;
		            else if ((preposition[0] - 3 == nowposition[0]) && (preposition[1] == nowposition[1]))
		               return 0;
		            else if ((preposition[0] + 2 == nowposition[0]) && (preposition[1] == nowposition[1]))
		               return 0;
		            else if ((preposition[0] + 3 == nowposition[0]) && (preposition[1] == nowposition[1]))
		               return 0;
		            else
		               return 1;
		         }
			
			/*ǳ���� �������� x��ǥ ���� 2�� ���� �Ǵ� y��ǥ ���� 2�� ���̰� ���� ǳ���̴� ǳ���̸� �������� x��ǥ ���� 3�� ���� �Ǵ� y��ǥ 3�� ���̳���
			 * ��ǥ�� �̵��� �� �ִ�.  */
			else if (board[preposition[0] - 2][preposition[1]] != 0) {
		            if ((preposition[0] - 3 == nowposition[0]) && (preposition[1] == nowposition[1]))
		               return 0;
		            else
		               return 1;
		         } else if (board[preposition[0] + 2][preposition[1]] != 0) {
		            if ((preposition[0] + 3 == nowposition[0]) && (preposition[1] == nowposition[1]))
		               return 0;
		            else
		               return 1;
		         } else if (board[preposition[0]][preposition[1] - 2] != 0) {
		            if ((preposition[0] == nowposition[0]) && (preposition[1] - 3 == nowposition[1]))
		               return 0;
		            else
		               return 1;
		         } else if (board[preposition[0]][preposition[1] + 2] != 0) {
		            if ((preposition[0] == nowposition[0]) && (preposition[1] + 3 == nowposition[1]))
		               return 0;
		            else
		               return 1;
		         }
		      
			}
		return 1;
	}
	
	/*�Ź��� �������� ����ϴ� �Լ��̴�. countSomeSpider�Լ��� ������� �ε�����, ���� �Ź��� ��ǥ, �Ź̰� ������ ��ǥ�� �Ű������� �޴´�.
	 * �Ź̴� �ν����� �����ϰ� �Ź̸� �������� �밢��1 ���⿡ �ε��� ���� ���ٸ�.�ִ� �밢�� �������� 2������ �̵��� �� �� �ִ�.*/
	public int countSomeSpider(int[][] board, int[] preposition, int[] nowposition) {
		
		if(((nowposition[0] == 2 || nowposition[0] == 9) && (nowposition[1] == 5 || nowposition[1] == 10)) 
				|| (nowposition[0] == 5 && nowposition[1] == 2) ||(nowposition[0] == 6 && nowposition [1] == 13)){
				JOptionPane.showConfirmDialog(null, "�ν������� �̵��Ͻ� �� �����ϴ�.", "---------------------���------------------",
						JOptionPane.WARNING_MESSAGE);
				return 1;
			}
		
		/*�Ź̸� �������� x��ǥy��ǥ �������� 2��ŭ�� �� �밢�� �������� ��ĭ�� �̵��� ��쿡 �Ź��� �����ӿ� �����ϹǷ� ����ǿ�  �Ź̰� ������ ���� ��ǥ���� �Ѱ��ش�.
		 * ���� �� ������ countSomeSpider�� ȣ���� �Լ����� ���Ǹ� �Ź��� �밢���� ���� ������� ������ �� �ִ�.*/
		if (nowposition[0] - preposition[0] == 2 && nowposition[1] - preposition[1] == 2) {
			return board[preposition[0] + 1][preposition[1] + 1];
		} else if (nowposition[0] - preposition[0] == -2 && nowposition[1] - preposition[1] == 2) {
			return board[preposition[0] - 1][preposition[1] + 1];
		} else if (nowposition[0] - preposition[0] == -2 && nowposition[1] - preposition[1] == -2) {
			return board[preposition[0] - 1][preposition[1] - 1];
		} else if (nowposition[0] - preposition[0] == 2 && nowposition[1] - preposition[1] == -2) {
			return board[preposition[0] + 1][preposition[1] - 1];
			/*�Ź̸� �������� x��ǥy��ǥ �������� 1��ŭ�� �� �밢�� �������� ��ĭ�� �̵��� ��쿡 �Ź��� �����ӿ� �����ϹǷ� ����ǿ�  �Ź̰� ������ ���� ��ǥ���� �Ѱ��ش�.*/	
		} else if (nowposition[0] - preposition[0] == 1 && nowposition[1] - preposition[1] == 1) {
			return 0;
		} else if (nowposition[0] - preposition[0] == 1 && nowposition[1] - preposition[1] == -1) {
			return 0;
		} else if (nowposition[0] - preposition[0] == -1 && nowposition[1] - preposition[1] == 1) {
			return 0;
		} else if (nowposition[0] - preposition[0] == -1 && nowposition[1] - preposition[1] == -1) {
			return 0;
		}
		else
			return 1;
	}
	public void candyplay(){ // �� �Լ��� ĵ������ ���� �Ǿ� ���� ���ھ ���� ��쿡 ����ϴ� �Լ��̴�.
	    try {
	     // File �� �ޱ�
	      File candy = new File("Music/candyZone.wav");
	      // �޾ƿ� File ������ ����� �Է� ��Ʈ���� ��ȯ��, ��Ÿ�� ���ڵ��� ����� �Է� ��Ʈ���� ��� 
	      AudioInputStream candyInputStream = AudioSystem.getAudioInputStream(candy);
	      
	      AudioFormat candyFormat = candyInputStream.getFormat();
	      // ����Ʈ���� �ƴϰ� ���� �����Ӽ��� ��Ÿ������, ��Ʈ���� ���̸� ���

	      // ������ ����� ������ ������ ������ �����κ��� ������ ������ ���� ������Ʈ�� ����
	      DataLine.Info candyinfo = new DataLine.Info(SourceDataLine.class,candyFormat);

	      SourceDataLine candyline = (SourceDataLine) AudioSystem.getLine(candyinfo);
	      // ������ Line.Info ������Ʈ�� ����� ��ġ�ϴ� ������ ���

	     // ������ ���İ� ������ ���� ������� ������ ����, ������ �ʿ��� system resource�� ȹ���� ���� ����
	      candyline.open(candyFormat);
	    // ���ο����� ������ ������� ����
	      candyline.start();

	      int nBytesRead = 0;
	      byte[] abData = new byte[128000];
	      while (nBytesRead != -1) {
	        nBytesRead = candyInputStream.read(abData, 0, abData.length);
	        if (nBytesRead >= 0) {
	          int nBytesWritten = candyline.write(abData, 0, nBytesRead);
	        }
	      }
	    }
	 catch (Exception e) {
	      e.printStackTrace();
	    }
	  }
	public void endplay(){ //������ ������ �� ���������� �����ϴ� �Լ��̴�.
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
	
	/*ĵ�������ھ�1 �Լ��� ���� �ε����� ���� ���� ��ǥ, ���� �̵��� ���� ��ǥ�� �Ű������� �޴´�. ĵ������ (5,7)(5,8)(6,7)(6,8)�� ��ǥ�� �����Ǿ� ������
	 * ĵ������ �� ���� ������ ĵ������ �� ������ ���� �ε��� ���� 2���� ������ ��´�. ���� ĵ�������� ������ �� ���� �������� ������ �ٽ� �����ȴ�. */
	public void candyZoneScore1(int board[][], int[] preposition, int[] nowposition){
		/*����� ��Ȳ���� ĵ������ �� ��� ������� ���ھ 2�� ���� �� �� ���갪�� ���ھ� �ǳڿ� ǥ�����ش�. ���� candyplay�Լ��� 
		 * ȣ��Ǿ ĵ������ �� ��� �ش�Ǵ� ������ ������ �ȴ�. */
		if(!((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				&&(((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8)))&&(KoreaChess.myTurn ==0)){
			Information.score1 += 2;
			scbar1 = new JLabel(" " +score1.toString()+" ");
			scbar1.setFont(new Font("�������",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar1);
			candyplay();
			}
		/*����� ��Ȳ���� ĵ������ ������ ��� ������� ���ھ 2�� ������  �� ���갪�� ���ھ� �ǳڿ� ǥ�����ش�.*/
		else if((((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				 &&(!((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8))))
					&&(KoreaChess.myTurn ==0)){
			Information.score1 -= 2;
			scbar1 = new JLabel(" " +score1.toString()+" ");
			scbar1.setFont(new Font("�������",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar1);
			
		}
		/*������ ��Ȳ���� ĵ������ �� ��� ������� ���ھ 2�� ���� �� �� ���갪�� ���ھ� �ǳڿ� ǥ�����ش�. ���� candyplay�Լ��� 
		 * ȣ��Ǿ ĵ������ �� ��� �ش�Ǵ� ������ ������ �ȴ�. */
		else if(!((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				&&(((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8)))&&(KoreaChess.myTurn ==1)){
			Information.score2 += 2;
			scbar2 = new JLabel(" " +score2.toString()+" ");
			scbar2.setFont(new Font("�������",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar2);
			candyplay();
			}
		/*������ ��Ȳ���� ĵ������ ������ ��� ������� ���ھ 2�� ������  �� ���갪�� ���ھ� �ǳڿ� ǥ�����ش�.*/
		else if((((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				 &&(!((nowposition[0] == 5 || nowposition[0] == 6) 
					&& (nowposition[1] == 7 || nowposition[1] == 8))))&&(KoreaChess.myTurn ==1)){
			Information.score2 -= 2;
			scbar2 = new JLabel(" " +score2.toString()+" ");
			scbar2.setFont(new Font("�������",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar2);
			
		}
		/*�� ���ھ 12���� �Ѱ� �Ǿ����� �� ���� �¸� ���� ������ ������ �ǰ� ������ ������� �˸��� �޼����� �Բ� ������ ����ȴ�.*/
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
	
	/*ĵ�������ھ�2 �Լ��� ���� �ε����� ���� ���� ��ǥ, ���� �̵��� ���� ��ǥ�� �Ű������� �޴´�. ĵ������ (5,7)(5,8)(6,7)(6,8)�� ��ǥ�� �����Ǿ� ������
	 * ĵ������ �� ���� ������ ĵ������ �� ������ ���� �ε��� ���� 2���� ������ ��´�. ���� ĵ�������� ������ �� ���� �������� ������ �ٽ� �����ȴ�. */
	public void candyZoneScore2(int board[][], int[] preposition, int[] nowposition){ // �Ź̰� ���ھ����� �� ��� +4 ������� -4
		/*����� ��Ȳ���� ĵ������ �� ��� ������� ���ھ 4�� ���� �� �� ���갪�� ���ھ� �ǳڿ� ǥ�����ش�. ���� candyplay�Լ��� 
		 * ȣ��Ǿ ĵ������ �� ��� �ش�Ǵ� ������ ������ �ȴ�. */
		if(!((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				&&(((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8)))&&(KoreaChess.myTurn ==0)){
			Information.score1 += 4;
			scbar1 = new JLabel(" " +score1.toString()+" ");
			scbar1.setFont(new Font("�������",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar1);
			candyplay();
			}
		/*����� ��Ȳ���� ĵ������ ������ ��� ������� ���ھ 4�� ������  �� ���갪�� ���ھ� �ǳڿ� ǥ�����ش�.*/
		else if((((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				 &&(!((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8))))
					&&(KoreaChess.myTurn ==0)){
			Information.score1 -= 4;
			scbar1 = new JLabel(" " +score1.toString()+" ");
			scbar1.setFont(new Font("�������",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar1);
			
		}
		/*������ ��Ȳ���� ĵ������ �� ��� ������� ���ھ 4�� ���� �� �� ���갪�� ���ھ� �ǳڿ� ǥ�����ش�. ���� candyplay�Լ��� 
		 * ȣ��Ǿ ĵ������ �� ��� �ش�Ǵ� ������ ������ �ȴ�. */
		else if(!((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				&&(((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8)))&&(KoreaChess.myTurn ==1)){
			Information.score2 += 4;
			scbar2 = new JLabel(" " +score2.toString()+" ");
			scbar2.setFont(new Font("�������",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar2);
			candyplay();
			}
		/*������ ��Ȳ���� ĵ������ ������ ��� ������� ���ھ 4�� ������  �� ���갪�� ���ھ� �ǳڿ� ǥ�����ش�.*/
		else if((((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				 &&(!((nowposition[0] == 5 || nowposition[0] == 6) 
					&& (nowposition[1] == 7 || nowposition[1] == 8))))&&(KoreaChess.myTurn ==1)){
			Information.score2 -= 4;
			scbar2 = new JLabel(" " +score2.toString()+" ");
			scbar2.setFont(new Font("�������",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar2);
			
		}
		
		/*�� ���ھ 12���� �Ѱ� �Ǿ����� �� ���� �¸� ���� ������ ������ �ǰ� ������ ������� �˸��� �޼����� �Բ� ������ ����ȴ�.*/
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
	/*ĵ�������ھ�3 �Լ��� ���� �ε����� ���� ���� ��ǥ, ���� �̵��� ���� ��ǥ�� �Ű������� �޴´�. ĵ������ (5,7)(5,8)(6,7)(6,8)�� ��ǥ�� �����Ǿ� ������
	 * ĵ������ �� ���� ������ ĵ������ �� ������ ���� �ε��� ���� 2���� ������ ��´�. ���� ĵ�������� ������ �� ���� �������� ������ �ٽ� �����ȴ�. */
	public void candyZoneScore3(int board[][], int[] preposition, int[] nowposition){ //ǳ���̰� ���ھ����� �� ��� +6, ������� -6
		/*����� ��Ȳ���� ĵ������ �� ��� ������� ���ھ 6�� ���� �� �� ���갪�� ���ھ� �ǳڿ� ǥ�����ش�. ���� candyplay�Լ��� 
		 * ȣ��Ǿ ĵ������ �� ��� �ش�Ǵ� ������ ������ �ȴ�. */
		if(!((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				&&(((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8)))&&(KoreaChess.myTurn ==0)){
			Information.score1 += 6;
			scbar1 = new JLabel(" " +score1.toString()+" ");
			scbar1.setFont(new Font("�������",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar1);
			candyplay();
			}
		/*����� ��Ȳ���� ĵ������ ������ ��� ������� ���ھ 6�� ������  �� ���갪�� ���ھ� �ǳڿ� ǥ�����ش�.*/
		else if((((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				 &&(!((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8))))
					&&(KoreaChess.myTurn ==0)){
			Information.score1 -= 6;
			scbar1 = new JLabel(" " +score1.toString()+" ");
			scbar1.setFont(new Font("�������",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar1);
			
		}
		/*������ ��Ȳ���� ĵ������ �� ��� ������� ���ھ 6�� ���� �� �� ���갪�� ���ھ� �ǳڿ� ǥ�����ش�. ���� candyplay�Լ��� 
		 * ȣ��Ǿ ĵ������ �� ��� �ش�Ǵ� ������ ������ �ȴ�. */
		else if(!((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				&&(((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8)))&&(KoreaChess.myTurn ==1)){
			Information.score2 += 6;
			scbar2 = new JLabel(" " +score2.toString()+" ");
			scbar2.setFont(new Font("�������",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar2);
			candyplay();
			}
		/*������ ��Ȳ���� ĵ������ ������ ��� ������� ���ھ 6�� ������  �� ���갪�� ���ھ� �ǳڿ� ǥ�����ش�.*/
		else if((((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				 &&(!((nowposition[0] == 5 || nowposition[0] == 6) 
					&& (nowposition[1] == 7 || nowposition[1] == 8))))&&(KoreaChess.myTurn ==1)){
			Information.score2 -= 6;
			scbar2 = new JLabel(" " +score2.toString()+" ");
			scbar2.setFont(new Font("�������",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar2);
			
		}
		/*�� ���ھ 12���� �Ѱ� �Ǿ����� �� ���� �¸� ���� ������ ������ �ǰ� ������ ������� �˸��� �޼����� �Բ� ������ ����ȴ�.*/
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
	/*ĵ�������ھ�4 �Լ��� ���� �ε����� ���� ���� ��ǥ, ���� �̵��� ���� ��ǥ�� �Ű������� �޴´�. ĵ������ (5,7)(5,8)(6,7)(6,8)�� ��ǥ�� �����Ǿ� ������
	 * ĵ������ �� ���� ������ ĵ������ �� ������ ���� �ε��� ���� 2���� ������ ��´�. ���� ĵ�������� ������ �� ���� �������� ������ �ٽ� �����ȴ�. */
	public void candyZoneScore4(int board[][], int[] preposition, int[] nowposition){ //ǳ���̰� ���ھ����� �� ��� +8, ������� -8
		/*����� ��Ȳ���� ĵ������ �� ��� ������� ���ھ 8�� ���� �� �� ���갪�� ���ھ� �ǳڿ� ǥ�����ش�. ���� candyplay�Լ��� 
		 * ȣ��Ǿ ĵ������ �� ��� �ش�Ǵ� ������ ������ �ȴ�. */
		if(!((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				&&(((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8)))&&(KoreaChess.myTurn ==0)){
			Information.score1 += 8;
			scbar1 = new JLabel(" " +score1.toString()+" ");
			scbar1.setFont(new Font("�������",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar1);
			candyplay();
			}
		/*����� ��Ȳ���� ĵ������ ������ ��� ������� ���ھ 8�� ������  �� ���갪�� ���ھ� �ǳڿ� ǥ�����ش�.*/
		else if((((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				 &&(!((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8))))
					&&(KoreaChess.myTurn ==0)){
			Information.score1 -= 8;
			scbar1 = new JLabel(" " +score1.toString()+" ");
			scbar1.setFont(new Font("�������",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar1);
			
		}
		/*������ ��Ȳ���� ĵ������ �� ��� ������� ���ھ 8�� ���� �� �� ���갪�� ���ھ� �ǳڿ� ǥ�����ش�. ���� candyplay�Լ��� 
		 * ȣ��Ǿ ĵ������ �� ��� �ش�Ǵ� ������ ������ �ȴ�. */
		else if(!((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				&&(((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8)))&&(KoreaChess.myTurn ==1)){
			Information.score2 += 8;
			scbar2 = new JLabel(" " +score2.toString()+" ");
			scbar2.setFont(new Font("�������",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar2);
			candyplay();
			}
		/*������ ��Ȳ���� ĵ������ ������ ��� ������� ���ھ 8�� ������  �� ���갪�� ���ھ� �ǳڿ� ǥ�����ش�.*/
		else if((((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				 &&(!((nowposition[0] == 5 || nowposition[0] == 6) 
					&& (nowposition[1] == 7 || nowposition[1] == 8))))&&(KoreaChess.myTurn ==1)){
			Information.score2 -= 8;
			scbar2 = new JLabel(" " +score2.toString()+" ");
			scbar2.setFont(new Font("�������",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar2);
			
		}
		/*�� ���ھ 12���� �Ѱ� �Ǿ����� �� ���� �¸� ���� ������ ������ �ǰ� ������ ������� �˸��� �޼����� �Բ� ������ ����ȴ�.*/
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
}
