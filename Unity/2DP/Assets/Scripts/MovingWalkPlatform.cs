using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MovingWalkPlatform : PlatformBase
{
    public Vector2 moveVector;

    //매 fixedUpdate 때마다 발생
    private void OnTriggerStay2D(Collider2D other)
    {
        if (other.CompareTag("Player"))
        {
            //other.transform.position += (Vector3)moveVector * Time.fixedDeltaTime;
            other.GetComponent<Rigidbody2D>().AddForce(moveVector, ForceMode2D.Force);
        }
    }

    private void OnTriggerExit2D(Collider2D other)
    {
        Rigidbody2D playerRigid = other.GetComponent<Rigidbody2D>();
        playerRigid.velocity = new Vector2(moveVector.x != 0 ? 0 : playerRigid.velocity.x
                                           , moveVector.y != 0 ? 0 : playerRigid.velocity.y);
    }
}
