using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerCtrl : MonoBehaviour
{
    //컴포넌트를 캐시 처리할 변수
    private Transform tr;
    //Animation 컴포넌트를 저장할 변수
    private Animation anim;

    //이동 속도 변수 (public으로 선언되어 인스펙터 뷰에 노출됨)
    public float moveSpeed = 10.0f;

    //회전 속도 변수
    public float turnSpeed = 80.0f;

    private readonly float initHp = 100.0f;

    public float currHp;

    public delegate void PlayerDieHandler();

    public static event PlayerDieHandler OnPlayerDie;

    private Image hpBar;

    // Start is called before the first frame update
    IEnumerator Start()
    {
        hpBar = GameObject.FindGameObjectWithTag("HP_BAR")?.GetComponent<Image>();

        currHp = initHp;
        DisplayHealth();

        //Transform 컴포넌트를 추출해 변수에 대입
        tr = GetComponent<Transform>();
        anim = GetComponent<Animation>();

        //애니메이션 실행
        anim.Play("Idle");

        turnSpeed = 0.0f;
        yield return new WaitForSeconds(0.3f);
        turnSpeed = 80.0f;

    }

    // Update is called once per frame
    void Update()
    {
        float h = Input.GetAxis("Horizontal"); // -1.0f ~ 0.0f ~ +1.0f
        float v = Input.GetAxis("Vertical"); // -1.0f ~ 0.0f ~ +1.0f
        float r = Input.GetAxis("Mouse X");

        //Debug.Log("h=" + h);
        //Debug.Log("v=" + v);

        //Transform 컴포넌트의 위치를 변경
        //transform.position += new Vector3(1f * h * Time.deltaTime, 0, 1f * v * Time.deltaTime);
        //tr.position += Vector3.forward * 1;
        //tr.Translate(new Vector3(
        //     1f * h * Time.deltaTime, 0, 1f * v * Time.deltaTime));
        Vector3 moveDir = (Vector3.forward * v) + (Vector3.right * h);
        tr.Translate(moveDir.normalized * moveSpeed * Time.deltaTime);

        tr.Rotate(Vector3.up * turnSpeed * Time.deltaTime * r);

        // 주인공 캐릭터의 애니메이션 설정
        PlayerAnim(h, v);
    }

    void PlayerAnim(float h, float v)
    {
        // 키보드 입력값을 기준으로 동작할 애니메이션 수행
        if (v >= 0.1f)
        {
            anim.CrossFade("RunF", 0.25f); // 전진 애니메이션 실행
        }
        else if (v <= -0.1f)
        {
            anim.CrossFade("RunB", 0.25f);// 후진 애니메이션 실행
        }
        else if (h >= 0.1f)
        {
            anim.CrossFade("RunR", 0.25f); // 오른쪽 애니메이션 실행
        }
        else if (h <= -0.1f)
        {
            anim.CrossFade("RunL", 0.25f); // 왼쪽 애니메이션 실행
        }
        else
        {
            anim.CrossFade("Idle", 0.25f); // 정지 애니메이션 실행
        }
    }

    private void OnTriggerEnter(Collider other)
    {
        if (currHp >= 0.0f && other.CompareTag("PUNCH"))
        {
            currHp -= 10.0f;
            DisplayHealth();

            Debug.Log($"Player hp = {currHp / initHp}");

            
        }
        if (currHp <= 0.0f)
        {
            PlayerDie();
        }
    }

    void PlayerDie()
    {
        Debug.Log("Player Die !");

        //GameObject[] monsters = GameObject.FindGameObjectsWithTag("MONSTER");

        //foreach(GameObject monster in monsters)
        //{
        //    monster.SendMessage("OnPlayerDie", SendMessageOptions.DontRequireReceiver);
        //}

        OnPlayerDie();

        //GameObject.Find("GameMgr").GetComponent<GameManager>().IsGameOver = true;
        GameManager.instance.IsGameOver = true;
    }

    void DisplayHealth()
    {
        hpBar.fillAmount = currHp / initHp;
    }
}
