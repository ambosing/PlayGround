using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SocialPlatforms;

public class Sensor : MonoBehaviour
{
    [Header("Sensor Setting")] 
    public float range = 4f;
    public float fov = 130f;
    public Transform sensorOrigin;
    public float sensorCheckCycle = 0.4f;
    [SerializeField, ReadOnly] private bool canCheck;

    /// <summary>
    /// 현재 인지하고 있는 적 캐릭터 리스트
    /// </summary>
    [ReadOnly] public List<FindPlayerInfo> currentFindTargets = new List<FindPlayerInfo>();

    /// <summary>
    /// FindTargets에 들어간 애들은 해당 시간이 지나면 잊혀진다.
    /// 잊혀지는 기준은 더 이상 시야각에 보이지 않을 떄부터 시간이 흐른다.
    /// </summary>
    public float timeToForget = 1f;

    private void Start()
    {
        canCheck = true;
        StartCoroutine(CheckSensor());
    }

    private void OnDrawGizmos()
    {
        Gizmos.color = Color.red;
        Gizmos.DrawWireSphere(transform.position, range);
        Gizmos.color = new Color(0f, 1f, 1f, 0.16f);
        Gizmos.DrawSphere(transform.position, range); 
        
        Vector3 leftDir = Quaternion.Euler(0f, -fov * 0.5f, 0f) * sensorOrigin.forward;
        Vector3 rightDir = Quaternion.Euler(0f, fov * 0.5f, 0f) * sensorOrigin.forward;
        
        Gizmos.color = new Color(0.2f, 1f, 0.37f, 1f);
        Gizmos.DrawRay(sensorOrigin.position, leftDir * range);
        Gizmos.DrawRay(sensorOrigin.position, rightDir * range);
    }

    private void Update()
    {
       
    }

    private void CheckFindPlayerExpire()
    {
        for (var index = currentFindTargets.Count - 1; index >= 0 ; index--)
        {
            var target = currentFindTargets[index];
            if (target.CheckExpire((timeToForget)))
                currentFindTargets.Remove(target);
        }
    }

    private IEnumerator CheckSensor()
    {
        while (true)
        {
            yield return new WaitForSeconds(sensorCheckCycle);
            CheckFindPlayerExpire();
            if (!canCheck) continue;
            Collider[] checkObjs = Physics.OverlapSphere(transform.position, range, 
                                                        LayerMask.GetMask("Player"));
            foreach (var checkObj in checkObjs)
            {
                Player targetPlayer = checkObj.GetComponent<Player>();
                Transform target = targetPlayer.targetedTransform;
                Vector3 dir = (target.position - transform.position).normalized;
                float dot = Vector3.Dot(dir, transform.forward);
                if (dot >= Mathf.Cos(fov * 0.5f))
                {
                    Debug.Log($"{checkObj}를 시야각 안에서 찾았따");
                    if (Physics.Linecast(sensorOrigin.transform.position, target.position,
                        LayerMask.GetMask("Default", "Ground"), QueryTriggerInteraction.Ignore))
                    {
                        Debug.Log($"{checkObj}를 찾았는데 시야각에 안에 있는데 안보인다.");
                    }
                    else
                    {
                        Vector3.MoveTowards(transform.position, target.position, 0.1f);
                        if (!currentFindTargets.Exists(x => x.player == targetPlayer))
                        {
                            currentFindTargets.Add(new FindPlayerInfo(targetPlayer));
                        }
                        else
                        {
                            currentFindTargets.Find(x => x.player == targetPlayer).UpdateFindTime();
                        }
                    }
                }
                else
                {
                    Debug.Log($"{checkObj}를 찾았는데 시야각에 없다.");
                }
            }
        }
    }
}
