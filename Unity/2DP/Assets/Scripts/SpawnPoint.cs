using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// 개발자가 실수하는 것을 방지
[RequireComponent(typeof(Collider2D))]
public class SpawnPoint : MonoBehaviour
{
    [SerializeField]
    private BoxCollider2D _collider2D;

    // 에디터 상에서만 쓰는 이벤트 함수
    private void Reset()
    {
        _collider2D = GetComponent<BoxCollider2D>();
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.CompareTag("Player"))
        {
            GameManager.Instance.spawnPoints.curSpawnPoint = this;
        }
    }

    // 아래의 함수도 매 프레임 실행된다.
    private void OnDrawGizmos()
    {
        Gizmos.color = Color.black;
        Gizmos.DrawWireCube(transform.position + (Vector3)_collider2D.offset, _collider2D.size);

    }
}
