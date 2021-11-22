using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using UnityEngine.SceneManagement;


/// <summary>
/// TODO: 1. PlayerPrefs 유니티에서 지원하는 데이터저장방식 장점은 쉽게 사용가능하다
/// TODO:   - 단점은 사용가능한 타입이 기본타입만 지원한다(INT, STRING, FLOAT)
/// TODO:   - 그래서 일일히 개별 타입으로 데이터를 저장해야해서 불편하고 구조체 저장이 불가하다.
/// TODO:   - 사람이 읽을 수 없는 형태로 저장되기 때문에 간편한 수정이 불가하다.
///
/// TODO: 2. 바이너리 형태로 저장하는 방식
/// TODO:   - 사람이 읽을 수 없는 형태로 저장되지만 속도가 매우 빠르고 직렬화 타입을 직접
/// TODO:   - 구현하면 모든 타입을 사용할 수 있다.
/// TODO:   - 직접 구현해야만 한다는게 단점이고 사람이 읽을 수 없는 형태이기 때문에 관리하는 툴이
/// TODO:   - 따로 필요하다.
///
/// TODO: 3. XML, Json, csv(+xlsx, xls)와 같은 텍스트 데이터 포맷으로 저장한다.
/// TODO:   - 사람이 읽을 수 있기 때문에 간편한 수정이 가능하다
/// TODO:   - 유니티에서 지원하는 기본 직렬화 타입은 바로 저장이 가능하고 구조체도 가능하다
/// TODO:   - 그 외에 필요한 타입이 있다면 직접 직렬화를 구현하면 추가적으로도 이용 가능하다.
/// TODO:   - 유니티는 JsonUtility를 지원하지만 LitJson, NewtonJson, MiniJson과 같은 라이브러리 이용 권장
///
/// TODO: 4. SQLite
/// TODO:   - 로컬에 파일형태로 저장되는 관계형 데이터베이스
/// TODO:   - 관계형 데이터베이스 형태로 이용하고 싶을 때 사용한다.
/// TODO:   - 요새는 잘 이용하지 않는 추세입니다.
/// 
/// TODO: 5. 외부 데이터베이스 활용
/// TODO:   - Redis, MongoDB와 같은 Nosql이나 Mysql, Mssql과 같은 관계형 데이터베이스를 포함한다.
/// TODO:   - 어찌되었던 외부의 머신에 있는 데이터베이스에 저장하는 방식
/// TODO:   - 장점은 보안과 속도(외부 머신에서 처리하기 때문), 관리(유저 데이터를 서버가 모두 가짐)
/// TODO:   - 단점은 관리(모두 관리해줘야한다.), 머신이 필요하다(현실적인 문제) -> AWS와 같은 클라우드 서비스 이용
/// </summary>
public class SaveLoadManager : MonoBehaviour
{
    public static SaveLoadManager Instance;
    public InitData initData;
    public int loadSlotIndex;

    private void Awake()
    {
        Instance = this;
        StartCoroutine(InitLoad());
    }

    [ContextMenu("Save")]
    public void Save()
    {
        SaveData saveData = new SaveData(13, transform.position, transform.rotation.eulerAngles);
        string saveDataString = JsonUtility.ToJson(saveData);
        string path = Application.dataPath + "/";
        string fileName = "SaveFile_" + TimeStamp;
        string fullPath = path + fileName + ".json";
        
        Debug.Log(saveDataString);

        // 새로운 세이브파일일 경우 초기데이터의 세이브파일 리스트에 추가 해준다.
        if (!File.Exists(fullPath))
        {
            if (initData == null)
                initData = new InitData();
            
            initData.saveFileList.Add(fileName);
            File.WriteAllText(path + "InitData.json", JsonUtility.ToJson(initData));
        }
            
        File.WriteAllText(fullPath, saveDataString);
    }
    
    
    private IEnumerator InitLoad()
    {
        yield return new WaitUntil(() => SceneManager.GetActiveScene().isLoaded);
        InitDataLoad();
        while (true)
        {
            yield return new WaitUntil(() => Input.GetKeyDown(KeyCode.S));
            SpecificFileLoad();
            yield return null;
        }
    }

    public void InitDataLoad()
    {
        string loadString = File.ReadAllText(Application.dataPath + "/InitData.json");
        InitData initData = JsonUtility.FromJson<InitData>(loadString);
        this.initData = initData;
    }

    [ContextMenu("SpecificFileLoad")]
    public void SpecificFileLoad()
    {
        string loadString = File.ReadAllText(Application.dataPath + "/" + initData.saveFileList[loadSlotIndex] + ".json");
        SaveData saveData = JsonUtility.FromJson<SaveData>(loadString);
        
        Transform player = transform;
        player.position = saveData.playerPos;
        player.rotation = Quaternion.Euler(saveData.playerRot);
        //player.level = saveData.level;
        
        Debug.Log("Player Level: " + saveData.level);
        Debug.Log("Player Pos: " + saveData.playerPos);
        Debug.Log("Player Rot: " + Quaternion.Euler(saveData.playerRot));
    }
    
    private long TimeStamp 
        => (long) (DateTime.UtcNow - new DateTime(1970, 1, 1, 0, 0, 0)).TotalSeconds;
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
    public SaveData(int level, Vector3 playerPos, Vector3 playerRot)
    {
        this.level = level;
        this.playerPos = playerPos;
        this.playerRot = playerRot;
    }

    public int level;
    public Vector3 playerPos;
    public Vector3 playerRot;
}
