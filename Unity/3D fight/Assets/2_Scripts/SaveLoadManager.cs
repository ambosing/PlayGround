using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;


// 1. PlayerPrefs
// - 유니티에서 지원하는 데이터저장방식 장점은 쉽게 저장이 가능하다.
// - 단점은 사용가능한 타입이 기본타입만 지원한다.(INT, STRING, FLOAT)
// - 그래서 일일히 개발 타입으로 데이터를 저장해야해서 불편하고 구조에 저장이 불가하다.
// - 사람이 읽을 수 있는 형태로 저장되기 때문에 간편한 수정이 불가하다.

// 2. 바이너리 형태로 저장하는 방식
// - 사람이 읽을 수 없는 형태로 저장되지만 속도가 매우 빠르고 직렬화 타입을 직접 구현하면 모든 타입을 사용할 수 있다.
// - 직접 구현해야만 한다는게 단점이고 사람이 읽을 수 없는 형태이기 때문에 관리하는 툴이 따로 필요하다.

// 3. JSON, XML, CSV와 같은 데이터 포맷으로 저장
// - 사람이 읽을 수 있기 때문에 간편한 수정이 가능하다.
// - 유니티에서 지원하는 기본 직렬화 타입은 바로 저장이 가능하고 구조체도 가능하다.
// - 그 외에 필요한 타입이 있다면 직접 직렬화를 구현하면 추가적으로도 이용 가능하다.
// - 유니티는 JsonUtility를 지원하지만 LitJson, NewtonJson, MiniJson과 같은 라이브러리 이용 권장

// 4. SQLite
// - 로컬에 파일형태로 저장되는 관계형 데이터베이스
// - 관계형 데이터베이스 형태로 이용하고 싶을 때 사용한다.
// - 요새는 잘 이용하지 않는 추세입니다. 클라우드에서 NoSQL로 구현되는 경우가 많고 데이터가 가변적인 경우가 더 좋다고 생각되기 때문에

// 5. 외부 데이터베이스 활용
// - Redis, MongoDB와 같은 NoSQL이나 MySQL, MSSQL과 같은 관계형 데이터베이스를 포함한다.
// - 외부의 머신에 있는 데이터베이스에 저장하는 방식
// - 장점은 보안과 속도(외부 머신에서 처리하기 때문), 관리(유저 데이터를 서버가 모두 가짐)
// - 단점은 관리(모두 관리해줘야한다.), 머신 필요하다(현실적인 문제) -> AWS, GCP와 같은 클라우드 서비스 이용
using System.IO;
using UnityEngine.SceneManagement;

public class SaveLoadManager : MonoBehaviour
{
    public static SaveLoadManager Instance;
    public InitData initData;
    public int loadSlotIndex;

    private void Awake()
    {
        Instance = this;
    }

    [ContextMenu("Save")]
    public void Save()
    {
        SaveData saveData = new SaveData(13, transform.position, transform.rotation.eulerAngles);
        string saveDataString = JsonUtility.ToJson(saveData);
        string fileName = "/SaveFile_" + TimeStamp;
        string path = Application.dataPath + fileName + ".json";
        
        Debug.Log(saveDataString);
        if (!File.Exists(path))
        {
            if (initData == null)
                initData = new InitData();
            initData.saveFileList.Add(path);
            File.WriteAllText(path + "InitData.json", JsonUtility.ToJson(initData));
        }            
        File.WriteAllText(path, saveDataString);
    }

    [ContextMenu("specificFileLoad")]
    public void SpecificFileLoad()
    {
        string loadString = File.ReadAllText(Application.dataPath + "/" + initData.saveFileList[loadSlotIndex] + ".json");
        SaveData saveData = JsonUtility.FromJson<SaveData>(loadString);
        Transform player = transform;
        player.position = saveData.playerPos;
        player.rotation = Quaternion.Euler(saveData.playerRot);
        //player.level = saveData.level;
        Debug.Log("Player Level : " + saveData.level);
        Debug.Log("Player position : " + saveData.playerPos);
        Debug.Log("Player rotation : " + saveData.playerRot);
    }

    private IEnumerator InitLoad()
    {
        yield return new WaitUntil(() => SceneManager.GetActiveScene().isLoaded);
        InitDataLoad();
        SpecificFileLoad();
    }
    
    public void InitDataLoad()
    {
        string loadString = File.ReadAllText(Application.dataPath + "/InitData.json");
        InitData initData = JsonUtility.FromJson<InitData>(loadString);
        this.initData = initData;
    }

    private long TimeStamp =>
        (long) (DateTime.UtcNow -
                new DateTime(1970,
                    1,
                    1,
                    0,
                    0,
                    0)).TotalSeconds;
}

[Serializable]
public class InitData
{
    public float masterVolume;
    public List<string> saveFileList;

    public InitData()
    {
        masterVolume = 0f;
        saveFileList = new List<string>();
    }

    public InitData(float masterVolume, List<string> saveFileList)
    {
        this.masterVolume = masterVolume;
        this.saveFileList = saveFileList;
    }
}


[Serializable]
public class SaveData
{
    public int level;
    public Vector3 playerPos;
    public Vector3 playerRot;

    public SaveData(int level, Vector3 playerPos, Vector3 playerRot)
    {
        this.level = level;
        this.playerPos = playerPos;
        this.playerRot = playerRot;
    }
}
