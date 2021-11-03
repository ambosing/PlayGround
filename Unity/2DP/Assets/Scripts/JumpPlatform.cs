using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class JumpPlatform : PlatformBase
{
    public Vector2 jumpVector;

    //Trigger 안에 Collider를 가진 객체가 들어오면 실행
    private void OnTriggerEnter2D(Collider2D collision)
    {
        Debug.Log($"{collision.name}이 들어옴");
        if (collision.CompareTag("Player"))
        {
            Rigidbody2D characterRigid = collision.GetComponent<Rigidbody2D>();
            characterRigid.velocity = new Vector2(0, 0);
            characterRigid.AddForce(jumpVector, ForceMode2D.Impulse);
        }
    }

    //private void OnTriggerStay2D(Collider2D collision)
    //{
    //    Debug.Log($"{collision.name}이 들어와있음");
    //}

    //private void OnTriggerExit2D(Collider2D collision)
    //{
    //    Debug.Log($"{collision.name}이 나갔음");
    //}
}
