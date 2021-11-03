using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ClearUI : MonoBehaviour
{
    public Text clearScoreText;
    public Text deadCountText;

    private void Awake()
    {
        
        if (gameObject.activeSelf)
            gameObject.SetActive(false);
    }

    public void OnClickExitGameButton()
    {
#if UNITY_EDITOR // 에디터 상에서 아래 코드
        UnityEditor.EditorApplication.isPlaying = false;
#elif Unity_WEBPLAYER // WEB 빌드 했을 떄

#else // 안드로이드, pc, ios 모두 먹히는 빌
#endif
    }

    public void Open()
    {
        clearScoreText.text = $"Score: {GameManager.Instance.GameScore}";
        deadCountText.text = $"Score: {GameManager.Instance.GameScore}";
        gameObject.SetActive(true);
        Time.timeScale = 0f;
        
    }
}
