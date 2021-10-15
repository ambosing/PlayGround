using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RemoveBullet : MonoBehaviour
{
    public GameObject sparkEffect;

    // 충돌이 시작할 때 발생하는 이벤트
    private void OnCollisionEnter(Collision collision)
    {


        //if (collision.collider.tag == "BULLET")
        if (collision.collider.CompareTag("BULLET"))
        {
            // 첫 번째 충돌 지점의 정보 추출
            ContactPoint cp = collision.GetContact(0);

            // 충돌한 총알의 법선 벡터를 쿼터니언 타입으로 변환
            Quaternion rot = Quaternion.LookRotation(-cp.normal);

            GameObject spark = Instantiate(sparkEffect, cp.point, rot);

            Destroy(collision.gameObject);

            Destroy(spark, 0.5f);
        }
    }
}
