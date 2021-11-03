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
	/*장기판의 좌표와, 말의 현재 좌표, 말이 이동할 나중좌표를 받아 boolean type로 반환. true면 움직임, false면 움직이지 않음.*/
	{
		
		if (i == 6 || i == 13) { // 애벌레 움직임 설정. 
			if (checkOneWorm(board, preposition, nowposition)) {
				return true;
			} else
				return false;
		} else if (i % 7 == 3) { // 풍뎅이 움직임 설정. countSomeBeetle가 0이되면 실행한다.
			if (countSomeBeetle(board, preposition, nowposition) == 0) {
				candyZoneScore3(board,preposition,nowposition);
				return true;
			} else
				return false;
		}

		else if (i % 7 == 5) { // 거미 움직임 설정 countsomeSpider가 0이 되면 실행한다.
			if (countSomeSpider(board, preposition, nowposition) == 0) {
				candyZoneScore2(board,preposition,nowposition);
				return true;
			} else
				return false;
		} 
		
		else if (i == 7) { // 파랑 개미 움직임 설정. 파란 개미는 y좌표를 기준으로 -값이 될 수 없다.
			if (checkOneAnt(board, preposition, nowposition) == 0) {
				if ((preposition[1] - nowposition[1]) <= 0) {
					candyZoneScore1(board,preposition,nowposition);
					return true;
				}
			}
			return false;
		} 
		
		else if (i == 14) { // 빨간개미 움직임 설정 뒤로 못간다. 빨간 개미는 y좌표를 기준으로 +값이 될 수 없다.
			if (checkOneAnt(board, preposition, nowposition) == 0) {
				if ((preposition[1] - nowposition[1]) >= 0) {
					candyZoneScore1(board,preposition,nowposition);
					return true;
				}
			}
			return false;
		}

		return true; //함수를 호출한 콜러에게 리턴값 true를 보내준다.
	}
	
	/*개미의 움직임을 설정하는 함수. 장기판의 인덱스와 현재 개미가 있는 위치, 개미가 움직일 곳의 좌표를 받는다.
	 개미가 움직일 x좌표의 차이와 y좌표의 차이를 가지고 수식을 세워 조건이 참이되면 개미가 움직일 좌표를 반환해준다.*/
	public int checkOneAnt(int[][] board, int[] preposition, int[] nowposition) {
		int a, b;

		a = preposition[0] - nowposition[0];
		b = preposition[1] - nowposition[1];
		
		/*부시존으로의 이동을 막는 조건문. 부시존의 좌표로 이동하게 될 경우 경고 메세지와 함께 리턴값1을 반환. 즉 움직이지 못한다.*/
		if(((nowposition[0] == 2 || nowposition[0] == 9) && (nowposition[1] == 5 || nowposition[1] == 10)) 
			|| (nowposition[0] == 5 && nowposition[1] == 2) ||(nowposition[0] == 6 && nowposition [1] == 13)){
			JOptionPane.showConfirmDialog(null, "부시존으로 이동하실 수 없습니다.", "---------------------경고------------------",
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
	
	/*애벌레의 움직임을 설정하는 함수. 장기판의 인덱스와 현재 애벌레가 있는 위치, 애벌레가 움직일 곳의 좌표를 받는다.
	 애벌레가 움직일 x좌표의 차이와 y좌표의 차이를 가지고 수식을 세워 조건이 참이되면 애벌레가 움직일 좌표를 반환해준다.*/
	public boolean checkOneWorm(int board[][], int[] preposition, int[] nowposition) {

		int a, b;

		a = preposition[0] - nowposition[0];
		b = preposition[1] - nowposition[1];
		
		if(((nowposition[0] == 2 || nowposition[0] == 9) && (nowposition[1] == 5 || nowposition[1] == 10)) 
				|| (nowposition[0] == 5 && nowposition[1] == 2) ||(nowposition[0] == 6 && nowposition [1] == 13)){
				JOptionPane.showConfirmDialog(null, "부시존으로 이동하실 수 없습니다.", "---------------------경고------------------",
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
	
	/*애벌레의 대각선 움직임을 설정하는 함수. 장기판의 인덱스와 현재 애벌레가 있는 위치, 애벌레가 움직일 곳의 좌표를 받는다.
	 애벌레가 움직일 x좌표의 차이와 y좌표의 차이를 가지고 수식을 세워 조건이 참이되면 애벌레가 움직일 좌표를 반환해준다.*/
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

	/*풍뎅이의 움직임을 설정하는 함수. 장기판의 인덱스와 현재 풍뎅이가 있는 위치, 풍뎅이가 움직일 곳의 좌표를 받는다.
	 애벌레가 움직일 x좌표의 차이와 y좌표의 차이를 가지고 수식을 세워 조건이 참이되면 애벌레가 움직일 좌표를 반환해준다.
	 */
	public int countSomeBeetle(int[][] board, int[] preposition, int[] nowposition) {
		/*풍뎅이의 x좌표가 0이였을때의 움직임 설정. 풍뎅이가 현재 있는 x,y 좌표 각각의 값에서 상하좌우 인덱스가 0이 아니면(비어있지 않으면) 
		 * 움직일 수 있음. 풍뎅이는 상하좌우 한칸 앞에 인덱스 값이 있으면 그 값의 최대 2의 차이를 내는 좌표로 움직일 수 있다.*/
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
		
		/*풍뎅이가 현재 있던 인덱스의 y좌표가 15였다면 y가 15 이상의 값으로는 넘어갈 수 없다.(장기판의 좌표를 넘어간다.)*/
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
		
		/*풍뎅이가 현재 있던 인덱스의 x좌표가 11였다면 x가 11 이상의 값으로는 넘어갈 수 없다.(장기판의 좌표를 넘어간다.)*/
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
		
		/*풍뎅이를 기준으로 상하좌우의 인덱스에 어떤 값이 있다면 풍뎅이는 움직일 수 있다. 즉 뛰어 넘을 수 있다. 풍뎅이가 움직일 좌표가 풍뎅이가 움직일 수
		 * 있는 범위라면 0값을 반환해준다. 함수를 호출한 콜러에게 0값을 리턴하게 되면 풍뎅이는 움직일 수 있다.   */
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
			
			/*풍뎅이 기준으로 x좌표 값이 2의 차이 또는 y좌표 값이 2의 차이가 나면 풍뎅이는 풍뎅이를 기준으로 x좌표 값의 3의 차이 또는 y좌표 3의 차이나는
			 * 좌표로 이동할 수 있다.  */
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
	
	/*거미의 움직임을 계산하는 함수이다. countSomeSpider함수는 장기판의 인덱스와, 현재 거미의 좌표, 거미가 움직일 좌표를 매개변수로 받는다.
	 * 거미는 부쉬존을 제외하고 거미를 기준으로 대각선1 방향에 인덱스 값이 없다면.최대 대각선 방향으로 2까지의 이동을 할 수 있다.*/
	public int countSomeSpider(int[][] board, int[] preposition, int[] nowposition) {
		
		if(((nowposition[0] == 2 || nowposition[0] == 9) && (nowposition[1] == 5 || nowposition[1] == 10)) 
				|| (nowposition[0] == 5 && nowposition[1] == 2) ||(nowposition[0] == 6 && nowposition [1] == 13)){
				JOptionPane.showConfirmDialog(null, "부시존으로 이동하실 수 없습니다.", "---------------------경고------------------",
						JOptionPane.WARNING_MESSAGE);
				return 1;
			}
		
		/*거미를 기준으로 x좌표y좌표 방향으로 2만큼씩 즉 대각선 방향으로 두칸을 이동할 경우에 거미의 움직임에 적합하므로 장기판에  거미가 움직일 곳의 좌표값을 넘겨준다.
		 * 이후 이 값들은 countSomeSpider를 호출한 함수에서 사용되며 거미의 대각선에 말이 없을경우 움직일 수 있다.*/
		if (nowposition[0] - preposition[0] == 2 && nowposition[1] - preposition[1] == 2) {
			return board[preposition[0] + 1][preposition[1] + 1];
		} else if (nowposition[0] - preposition[0] == -2 && nowposition[1] - preposition[1] == 2) {
			return board[preposition[0] - 1][preposition[1] + 1];
		} else if (nowposition[0] - preposition[0] == -2 && nowposition[1] - preposition[1] == -2) {
			return board[preposition[0] - 1][preposition[1] - 1];
		} else if (nowposition[0] - preposition[0] == 2 && nowposition[1] - preposition[1] == -2) {
			return board[preposition[0] + 1][preposition[1] - 1];
			/*거미를 기준으로 x좌표y좌표 방향으로 1만큼씩 즉 대각선 방향으로 두칸을 이동할 경우에 거미의 움직임에 적합하므로 장기판에  거미가 움직일 곳의 좌표값을 넘겨준다.*/	
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
	public void candyplay(){ // 이 함수는 캔디존에 들어가게 되어 더블 스코어를 얻을 경우에 출력하는 함수이다.
	    try {
	     // File 값 받기
	      File candy = new File("Music/candyZone.wav");
	      // 받아온 File 지정된 오디오 입력 스트림을 변환해, 나타난 인코딩의 오디오 입력 스트림을 취득 
	      AudioInputStream candyInputStream = AudioSystem.getAudioInputStream(candy);
	      
	      AudioFormat candyFormat = candyInputStream.getFormat();
	      // 바이트수는 아니고 샘플 프레임수로 나타내지는, 스트림의 길이를 취득

	      // 단일의 오디오 형식을 포함한 지정한 정보로부터 데이터 라인의 정보 오브젝트를 구축
	      DataLine.Info candyinfo = new DataLine.Info(SourceDataLine.class,candyFormat);

	      SourceDataLine candyline = (SourceDataLine) AudioSystem.getLine(candyinfo);
	      // 지정된 Line.Info 오브젝트의 기술에 일치하는 라인을 취득

	     // 지정된 형식과 지정된 버퍼 사이즈로 라인을 열어, 라인이 필요한 system resource를 획득해 조작 가능
	      candyline.open(candyFormat);
	    // 라인에서의 데이터 입출력을 가능
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
	public void endplay(){ //게임이 끝났을 때 종료음악을 실행하는 함수이다.
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
	
	/*캔디존스코어1 함수는 말의 인덱스와 말의 현재 좌표, 말이 이동할 나중 좌표를 매개변수로 받는다. 캔디존은 (5,7)(5,8)(6,7)(6,8)의 좌표로 구성되어 있으며
	 * 캔디존에 들어가 있을 동안은 캔디존에 들어간 말들이 가진 인덱스 값의 2배의 점수를 얻는다. 말이 캔디존에서 나오게 될 경우는 더해졌던 점수가 다시 감점된다. */
	public void candyZoneScore1(int board[][], int[] preposition, int[] nowposition){
		/*블루팀 상황에서 캔디존에 들어갈 경우 블루팀의 스코어에 2를 더한 후 그 연산값을 스코어 판넬에 표현해준다. 또한 candyplay함수가 
		 * 호출되어서 캔디존에 들어갈 경우 해당되는 음악이 나오게 된다. */
		if(!((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				&&(((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8)))&&(KoreaChess.myTurn ==0)){
			Information.score1 += 2;
			scbar1 = new JLabel(" " +score1.toString()+" ");
			scbar1.setFont(new Font("맑은고딕",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar1);
			candyplay();
			}
		/*블루팀 상황에서 캔디존에 나오게 경우 블루팀의 스코어에 2를 빼준후  그 연산값을 스코어 판넬에 표현해준다.*/
		else if((((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				 &&(!((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8))))
					&&(KoreaChess.myTurn ==0)){
			Information.score1 -= 2;
			scbar1 = new JLabel(" " +score1.toString()+" ");
			scbar1.setFont(new Font("맑은고딕",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar1);
			
		}
		/*레드팀 상황에서 캔디존에 들어갈 경우 블루팀의 스코어에 2를 더한 후 그 연산값을 스코어 판넬에 표현해준다. 또한 candyplay함수가 
		 * 호출되어서 캔디존에 들어갈 경우 해당되는 음악이 나오게 된다. */
		else if(!((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				&&(((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8)))&&(KoreaChess.myTurn ==1)){
			Information.score2 += 2;
			scbar2 = new JLabel(" " +score2.toString()+" ");
			scbar2.setFont(new Font("맑은고딕",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar2);
			candyplay();
			}
		/*레드팀 상황에서 캔디존에 나오게 경우 블루팀의 스코어에 2를 빼준후  그 연산값을 스코어 판넬에 표현해준다.*/
		else if((((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				 &&(!((nowposition[0] == 5 || nowposition[0] == 6) 
					&& (nowposition[1] == 7 || nowposition[1] == 8))))&&(KoreaChess.myTurn ==1)){
			Information.score2 -= 2;
			scbar2 = new JLabel(" " +score2.toString()+" ");
			scbar2.setFont(new Font("맑은고딕",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar2);
			
		}
		/*총 스코어가 12점을 넘게 되었으면 각 팀의 승리 축하 음악이 나오게 되고 게임이 종료됨을 알리는 메세지와 함께 게임이 종료된다.*/
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
	
	/*캔디존스코어2 함수는 말의 인덱스와 말의 현재 좌표, 말이 이동할 나중 좌표를 매개변수로 받는다. 캔디존은 (5,7)(5,8)(6,7)(6,8)의 좌표로 구성되어 있으며
	 * 캔디존에 들어가 있을 동안은 캔디존에 들어간 말들이 가진 인덱스 값의 2배의 점수를 얻는다. 말이 캔디존에서 나오게 될 경우는 더해졌던 점수가 다시 감점된다. */
	public void candyZoneScore2(int board[][], int[] preposition, int[] nowposition){ // 거미가 스코어존에 들어갈 경우 +4 나갈경우 -4
		/*블루팀 상황에서 캔디존에 들어갈 경우 블루팀의 스코어에 4를 더한 후 그 연산값을 스코어 판넬에 표현해준다. 또한 candyplay함수가 
		 * 호출되어서 캔디존에 들어갈 경우 해당되는 음악이 나오게 된다. */
		if(!((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				&&(((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8)))&&(KoreaChess.myTurn ==0)){
			Information.score1 += 4;
			scbar1 = new JLabel(" " +score1.toString()+" ");
			scbar1.setFont(new Font("맑은고딕",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar1);
			candyplay();
			}
		/*블루팀 상황에서 캔디존에 나오게 경우 블루팀의 스코어에 4를 빼준후  그 연산값을 스코어 판넬에 표현해준다.*/
		else if((((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				 &&(!((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8))))
					&&(KoreaChess.myTurn ==0)){
			Information.score1 -= 4;
			scbar1 = new JLabel(" " +score1.toString()+" ");
			scbar1.setFont(new Font("맑은고딕",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar1);
			
		}
		/*레드팀 상황에서 캔디존에 들어갈 경우 블루팀의 스코어에 4를 더한 후 그 연산값을 스코어 판넬에 표현해준다. 또한 candyplay함수가 
		 * 호출되어서 캔디존에 들어갈 경우 해당되는 음악이 나오게 된다. */
		else if(!((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				&&(((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8)))&&(KoreaChess.myTurn ==1)){
			Information.score2 += 4;
			scbar2 = new JLabel(" " +score2.toString()+" ");
			scbar2.setFont(new Font("맑은고딕",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar2);
			candyplay();
			}
		/*레드팀 상황에서 캔디존에 나오게 경우 블루팀의 스코어에 4를 빼준후  그 연산값을 스코어 판넬에 표현해준다.*/
		else if((((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				 &&(!((nowposition[0] == 5 || nowposition[0] == 6) 
					&& (nowposition[1] == 7 || nowposition[1] == 8))))&&(KoreaChess.myTurn ==1)){
			Information.score2 -= 4;
			scbar2 = new JLabel(" " +score2.toString()+" ");
			scbar2.setFont(new Font("맑은고딕",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar2);
			
		}
		
		/*총 스코어가 12점을 넘게 되었으면 각 팀의 승리 축하 음악이 나오게 되고 게임이 종료됨을 알리는 메세지와 함께 게임이 종료된다.*/
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
	/*캔디존스코어3 함수는 말의 인덱스와 말의 현재 좌표, 말이 이동할 나중 좌표를 매개변수로 받는다. 캔디존은 (5,7)(5,8)(6,7)(6,8)의 좌표로 구성되어 있으며
	 * 캔디존에 들어가 있을 동안은 캔디존에 들어간 말들이 가진 인덱스 값의 2배의 점수를 얻는다. 말이 캔디존에서 나오게 될 경우는 더해졌던 점수가 다시 감점된다. */
	public void candyZoneScore3(int board[][], int[] preposition, int[] nowposition){ //풍뎅이가 스코어존에 들어갈 경우 +6, 나갈경우 -6
		/*블루팀 상황에서 캔디존에 들어갈 경우 블루팀의 스코어에 6를 더한 후 그 연산값을 스코어 판넬에 표현해준다. 또한 candyplay함수가 
		 * 호출되어서 캔디존에 들어갈 경우 해당되는 음악이 나오게 된다. */
		if(!((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				&&(((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8)))&&(KoreaChess.myTurn ==0)){
			Information.score1 += 6;
			scbar1 = new JLabel(" " +score1.toString()+" ");
			scbar1.setFont(new Font("맑은고딕",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar1);
			candyplay();
			}
		/*블루팀 상황에서 캔디존에 나오게 경우 블루팀의 스코어에 6를 빼준후  그 연산값을 스코어 판넬에 표현해준다.*/
		else if((((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				 &&(!((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8))))
					&&(KoreaChess.myTurn ==0)){
			Information.score1 -= 6;
			scbar1 = new JLabel(" " +score1.toString()+" ");
			scbar1.setFont(new Font("맑은고딕",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar1);
			
		}
		/*레드팀 상황에서 캔디존에 들어갈 경우 블루팀의 스코어에 6을 더한 후 그 연산값을 스코어 판넬에 표현해준다. 또한 candyplay함수가 
		 * 호출되어서 캔디존에 들어갈 경우 해당되는 음악이 나오게 된다. */
		else if(!((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				&&(((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8)))&&(KoreaChess.myTurn ==1)){
			Information.score2 += 6;
			scbar2 = new JLabel(" " +score2.toString()+" ");
			scbar2.setFont(new Font("맑은고딕",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar2);
			candyplay();
			}
		/*레드팀 상황에서 캔디존에 나오게 경우 블루팀의 스코어에 6를 빼준후  그 연산값을 스코어 판넬에 표현해준다.*/
		else if((((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				 &&(!((nowposition[0] == 5 || nowposition[0] == 6) 
					&& (nowposition[1] == 7 || nowposition[1] == 8))))&&(KoreaChess.myTurn ==1)){
			Information.score2 -= 6;
			scbar2 = new JLabel(" " +score2.toString()+" ");
			scbar2.setFont(new Font("맑은고딕",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar2);
			
		}
		/*총 스코어가 12점을 넘게 되었으면 각 팀의 승리 축하 음악이 나오게 되고 게임이 종료됨을 알리는 메세지와 함께 게임이 종료된다.*/
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
	/*캔디존스코어4 함수는 말의 인덱스와 말의 현재 좌표, 말이 이동할 나중 좌표를 매개변수로 받는다. 캔디존은 (5,7)(5,8)(6,7)(6,8)의 좌표로 구성되어 있으며
	 * 캔디존에 들어가 있을 동안은 캔디존에 들어간 말들이 가진 인덱스 값의 2배의 점수를 얻는다. 말이 캔디존에서 나오게 될 경우는 더해졌던 점수가 다시 감점된다. */
	public void candyZoneScore4(int board[][], int[] preposition, int[] nowposition){ //풍뎅이가 스코어존에 들어갈 경우 +8, 나갈경우 -8
		/*블루팀 상황에서 캔디존에 들어갈 경우 블루팀의 스코어에 8를 더한 후 그 연산값을 스코어 판넬에 표현해준다. 또한 candyplay함수가 
		 * 호출되어서 캔디존에 들어갈 경우 해당되는 음악이 나오게 된다. */
		if(!((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				&&(((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8)))&&(KoreaChess.myTurn ==0)){
			Information.score1 += 8;
			scbar1 = new JLabel(" " +score1.toString()+" ");
			scbar1.setFont(new Font("맑은고딕",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar1);
			candyplay();
			}
		/*블루팀 상황에서 캔디존에 나오게 경우 블루팀의 스코어에 8를 빼준후  그 연산값을 스코어 판넬에 표현해준다.*/
		else if((((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				 &&(!((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8))))
					&&(KoreaChess.myTurn ==0)){
			Information.score1 -= 8;
			scbar1 = new JLabel(" " +score1.toString()+" ");
			scbar1.setFont(new Font("맑은고딕",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar1);
			
		}
		/*레드팀 상황에서 캔디존에 들어갈 경우 블루팀의 스코어에 8를 더한 후 그 연산값을 스코어 판넬에 표현해준다. 또한 candyplay함수가 
		 * 호출되어서 캔디존에 들어갈 경우 해당되는 음악이 나오게 된다. */
		else if(!((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				&&(((nowposition[0] == 5 || nowposition[0] == 6) && (nowposition[1] == 7 || nowposition[1] == 8)))&&(KoreaChess.myTurn ==1)){
			Information.score2 += 8;
			scbar2 = new JLabel(" " +score2.toString()+" ");
			scbar2.setFont(new Font("맑은고딕",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar2);
			candyplay();
			}
		/*레드팀 상황에서 캔디존에 나오게 경우 블루팀의 스코어에 8를 빼준후  그 연산값을 스코어 판넬에 표현해준다.*/
		else if((((preposition[0] == 5 || preposition[0] == 6) && (preposition[1] == 7 || preposition[1] == 8))
				 &&(!((nowposition[0] == 5 || nowposition[0] == 6) 
					&& (nowposition[1] == 7 || nowposition[1] == 8))))&&(KoreaChess.myTurn ==1)){
			Information.score2 -= 8;
			scbar2 = new JLabel(" " +score2.toString()+" ");
			scbar2.setFont(new Font("맑은고딕",Font.BOLD, 60));
			PlayerPanel[KoreaChess.myTurn].removeAll();
			PlayerPanel[KoreaChess.myTurn].add(scbar2);
			
		}
		/*총 스코어가 12점을 넘게 되었으면 각 팀의 승리 축하 음악이 나오게 되고 게임이 종료됨을 알리는 메세지와 함께 게임이 종료된다.*/
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
}
